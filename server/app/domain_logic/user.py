from typing import Dict

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema

NEARBY_DISTANCE_SETTING = 5.0 # Distance in miles.

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
    user.update(latitude=data['latitude'])
    user.update(longitude=data['longitude'])
    user.save()
    return user


def get_nearby_users(user_id: str) -> list:
    """
    Query and filter the list of users.
    
    Performs a linear distance query and then runs a haversine formula function 
    to deal with shrinking latitude width at the poles and distance on a spherical surface.
    """
    user = User.objects.get(id=user_id)
    
    nearby_positions = __calculate_nearby_positions(user)

    query = {
            '$or': [
                {'user.longitude': {'$gt': nearby_positions['longitude_minimum']}},
                {'user.longitude': {'$lt': nearby_positions['longitude_maximum']}}
            ]  
        }
    if (nearby_positions['use_latitude']):
        query = {
            '$and': [
                query, # insert longitude filter
                {'$or': [
                    {'user.latitude': {'$gt': nearby_positions['latitude_minimum']}},
                    {'user.latitude': {'$lt': nearby_positions['latitude_maximum']}}
                ]}  
            ]
        }

    users = User.objects.find(query)
    return users


def __calculate_nearby_positions(user: User) -> dict:
    """Calculate the latitude and longitude needed to query nearby entities."""
    nearby_positions = {}
    nearby_positions['use_latitude'] = True
    nearby_positions['latitude_minimum'] = user.latitude - NEARBY_DISTANCE_SETTING
    if (nearby_positions['latitude_minimum'] < -180):
        nearby_positions['latitude_minimum'] = nearby_positions['latitude_minimum'] + 360
    nearby_positions['longitude_minimum'] = user.longitude - NEARBY_DISTANCE_SETTING
    if (nearby_positions['longitude_minimum'] < -90):
        nearby_positions['use_latitude'] = False
        nearby_positions['longitude_minimum'] = -90
    nearby_positions['latitude_maximum'] = user.latitude + NEARBY_DISTANCE_SETTING
    if (nearby_positions['latitude_maximum'] > 180):
        nearby_positions['latitude_maximum'] = nearby_positions['latitude_maximum'] - 360
    nearby_positions['longitude_maximum'] = user.longitude + NEARBY_DISTANCE_SETTING
    if (nearby_positions['longitude_maximum'] > 90):
        nearby_positions['use_latitude'] = False
        nearby_positions['longitude_maximum'] = 90
    return nearby_positions

