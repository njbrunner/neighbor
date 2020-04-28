"""Endpoints for Neighbor database model."""

from flask import Blueprint, jsonify, request

from app.domain_logic import neighbor_domain_logic
from app.schemas.neighbor import neighbor_schema

NEIGHBOR_BP = Blueprint('neighbor_bp', __name__, url_prefix='/neighbor')


@NEIGHBOR_BP.route('/create', methods=["POST"])
def create():
    """Creates and saves a new instance of a neighbor relationship."""
    neighbor = neighbor_domain_logic.create_neighbor(request.json)
    return neighbor_schema.dump(neighbor)


@NEIGHBOR_BP.route('/<neighbor_id>', methods=['GET'])
def get_neighbors(user_id: str, page: int, page_size: int):
    """Retrieves neighbors for a given user."""
    neighbors = neighbor_domain_logic.get_neighbors(user_id, page, page_size)
    return jsonify([neighbor_schema.dump(neighbor) for neighbor in neighbors])
