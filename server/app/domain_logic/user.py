from typing import Dict, List

from flask_jwt_extended import get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema
from app.utilities import generate_access_token, create_twilio_user

RADIAN_DENOMINATOR = 0.62137  # Miles in a kilometer. Set to 1.609344 for kilometers to miles.
NEARBY_DISTANCE_SETTING = 5.0 / RADIAN_DENOMINATOR  # Distance in miles converted to kilometers.


def signup(user_data: UserSchema) -> User:
    """Save new user to database."""
    new_user_password = user_data.pop('password')
    user_data['hashed_password'] = generate_password_hash(new_user_password)
    new_user = User(**user_data)
    new_user.save()
    new_user.twilio_token = generate_access_token(identity=str(new_user.id))
    new_user.save()

    # Create Twilio user
    create_twilio_user(str(new_user.id), new_user.name)

    return new_user


def login(user_data: LoginSchema) -> User:
    """Authenticate existing user."""
    user = User.objects.get(email=user_data['email'])

    if check_password_hash(user.hashed_password, user_data['password']):
        user.twilio_token = generate_access_token(identity=str(user.id))
        user.save()
        return user

    raise Exception


def update_user_location(data: Dict[str, str]) -> User:
    """Update user location."""
    user = get_user()
    # TODO: Test if you need .update
    user.update(location={'type': 'Point', 'coordinates': [data['longitude'], data['latitude']]})
    user.location_identified = True
    user.save()
    return user


def get_potential_neighbors() -> List[User]:
    """
    Query and filter the list of users.

    Returns a list of Users.
    """
    user = get_user()

    users = User.objects(
        location__near=user.location['coordinates'],
        location__max_distance=NEARBY_DISTANCE_SETTING,
        role__ne=user.role,
        id__nin=[neighbor.id for neighbor in user.neighbors]
        + [neighbor.id for neighbor in user.blacklisted_neighbors]
    )
    return users


def get_user(user_id: str = None) -> User:
    if (not user_id):
        user_id = get_jwt_identity()
    return User.objects.get(id=user_id)


def get_neighbors():
    """Get the collection of neighbors for a user."""
    user = get_user()
    return user.neighbors


def add_neighbor(neighbor_id: str) -> None:
    """Add a user to the tracked neighbors so they don't appear in potential neighbor queries."""
    user = get_user()
    neighbor = get_user(neighbor_id)

    user.update(add_to_set__neighbors=neighbor)
    neighbor.update(add_to_set__neighbors=user)


def black_list_neighbor(neighbor_id: str) -> None:
    """Black lists a neighbor from the tracked neighbors so they don't appear in potential neighbor
    queries.

    Note that this is unidirectional and it does not update the neighbor to be joined with this
    user.
    """
    user = get_user()
    neighbor = get_user(neighbor_id)

    user.update(pull__neighbors=neighbor)
    user.update(add_to_set__blacklisted_neighbors=neighbor)
