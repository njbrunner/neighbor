"""Data access layer for Neighbor model."""

from typing import Dict, List
from mongoengine import Q

from app.models import Neighbor, User
from app.schemas import neighbor_schema


def create_neighbor(data: Dict[str, str]) -> Neighbor:
    """Save new neighbor to database."""
    new_neighbor = neighbor_schema.load(data)
    new_neighbor.save()
    User.objects.get(new_neighbor)
    return new_neighbor

def get_neighbors(user_id, page: int = 0, page_size: int = 10) -> List(Neighbor):
    """Retrieve pages of a user's neighbors."""
    neighbors = Neighbor.objects.filter( 
            (Q(seeker=user_id) or Q(provider=user_id)) 
        ).order_by('-last_contact') \
        .paginate(page=page, per_page=page_size)
    return neighbors

def get_neighbor_distance(seeker_id: str, provider_id: str) -> float:
    seeker = User.objects.get(unique_identity = seeker_id)
    # Validate user is a seeker?
    provider = User.objects(
        location__near=seeker.location['coordinates'],
        unique_identity=provider_id
    )
    # Validate user is a provider?
    return provider.dist['calculated']