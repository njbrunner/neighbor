from typing import Dict, List

from werkzeug.security import check_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema
from app.utilities import generate_access_token

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
        token = generate_access_token(identity=user.unique_identity)
        user.auth_token = token
        user.save()
        return user

    raise Exception


def update_user_location(user_id: str, data: Dict[str, str]) -> User:
    """Update user location."""
    user = User.objects.get(id=user_id)
    user.update(location={'type': 'Point', 'coordinates': [data['longitude'], data['latitude']]})
    user.location_identified = True
    user.save()
    return user


def get_nearby_users(user_id: str) -> List[User]:
    """
    Query and filter the list of users.

    Returns a list of Users.
    """
    user = User.objects.get(id=user_id)

    print(User.objects())

    users = User.objects(
        location__near=user.location['coordinates'],
        location__max_distance=NEARBY_DISTANCE_SETTING,
        role__ne=user.role
    )
    print(users)
    print(NEARBY_DISTANCE_SETTING)
    return users
