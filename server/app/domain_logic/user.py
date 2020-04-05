from typing import Dict

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models import User
# from app.schemas import LoginSchema, UserSchema
from app.schemas.user import LoginSchema, UserSchema


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
