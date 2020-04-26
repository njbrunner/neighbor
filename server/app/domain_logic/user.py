from typing import Dict

from werkzeug.security import check_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema
from app.utilities import generate_access_token


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
    user.update(latitude=data['latitude'])
    user.update(longitude=data['longitude'])
    user.save()
    return user
