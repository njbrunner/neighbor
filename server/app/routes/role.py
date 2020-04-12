"""Endpoints for Role database model."""

from flask import Blueprint

from app.domain_logic import role_domain_logic
from app.schemas.user import RoleSchema

ROLE_BP = Blueprint('role_bp', __name__, url_prefix='/role')


@ROLE_BP.route('/', methods=["GET"])
def get_roles():
    roles = role_domain_logic.get_roles()
    serialized_roles = [RoleSchema().dump(role) for role in roles]
    return {"roles": serialized_roles}
