from typing import Dict, List

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema

RADIAN_DENOMINATOR = 0.62137 # Miles in a kilometer. Set to 1.609344 for kilometers to miles.
NEARBY_DISTANCE_SETTING = 5.0 / RADIAN_DENOMINATOR # Distance in miles converted to kilometers.

def signup(data: Dict[str, str]) -> User:
    """Save new user to database."""
    new_user = UserSchema().load(data)
    new_user.save()
    return new_user


def login(data: Dict[str, str]) -> User:
    """Authenticate existing user."""
    serialized_login_data = LoginSchema().load(data)
    user = User.objects.get(email=serialized_login_data['email'])

    if check_password_hash(user.hashed_password, serialized_login_data['password']):
        user.auth_token = create_access_token(identity=user.email)
        user.save()
        return user

    raise Exception


def update_user_location(user_id: str, data: Dict[str, str]) -> User:
    """Update user location."""
    user = User.objects.get(id=user_id)
    user.update(location={'type': 'Point', 'coordinates': [data['longitude'], data['latitude']]})
    user.save()
    return user


def get_nearby_users(user_id: str) -> List[User]:
    """
    Query and filter the list of users.

    Returns a list of Users.
    """
    user = User.objects.get(id=user_id)

    query = {
        '$and': [
            {'$near': {
                '$geometry': user.location,
                '$maxDistance': NEARBY_DISTANCE_SETTING,
            }},
            {'user.role': {'$not': user.role}}
        ]
    }

    users = User.objects(query)
    return users
