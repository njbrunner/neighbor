from typing import Dict, List

from werkzeug.security import check_password_hash

from app.models import User
from app.schemas import LoginSchema, UserSchema
from app.utilities import generate_access_token, create_twilio_user

RADIAN_DENOMINATOR = 0.62137 # Miles in a kilometer. Set to 1.609344 for kilometers to miles.
NEARBY_DISTANCE_SETTING = 5.0 / RADIAN_DENOMINATOR # Distance in miles converted to kilometers.

def signup(data: Dict[str, str]) -> User:
    """Save new user to database."""
    new_user = UserSchema().load(data)
    new_user.save()

    # Create Twilio user
    create_twilio_user(new_user.unique_identity, new_user.name)

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


def get_potential_neighbors(user_id: str) -> List[User]:
    """
    Query and filter the list of users.

    Returns a list of Users.
    """
    user = User.objects.get(unique_identity=user_id)

    users = User.objects(
        location__near=user.location['coordinates'],
        location__max_distance=NEARBY_DISTANCE_SETTING,
        role__ne=user.role,
        unique_identity__nin=[ neighbor.unique_identity for neighbor in user.neighbors ]
            + [ neighbor.unique_identity for neighbor in user.blacklisted_neighbors ]
    )
    return users


def get_neighbors(user_id: str):
    """Get the collection of neighbors for a user."""
    user = User.objects.get(unique_identity=user_id)
    return user.neighbors

    
def add_neighbor(current_user_id: str, neighbor_id: str) -> None:
    """
    Adds a user to the tracked neighbors so they don't appear in potential neighbor queries.
    
    Note that this is unidirectional and it does not update the neighbor to be joined with this user.
    """
    user = User.objects.get(unique_identity=current_user_id)
    neighbor = User.objects.get(unique_identity=neighbor_id)

    user.update(add_to_set__neighbors=neighbor)

    
def black_list_neighbor(current_user_id: str, neighbor_id: str) -> None:
    """
    Black lists a neighbor from the tracked neighbors so they don't appear in potential neighbor queries.
    
    Note that this is unidirectional and it does not update the neighbor to be joined with this user.
    """
    user = User.objects.get(unique_identity=current_user_id)
    neighbor = User.objects.get(unique_identity=neighbor_id)

    user.update(pull__neighbors=neighbor)
    user.update(add_to_set__blacklisted_neighbors=neighbor)
