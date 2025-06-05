from http import HTTPStatus
from flask import Blueprint, request
from src.app import db, Role

bp = Blueprint('role', __name__, url_prefix='/roles')

def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()

def _list_roles():
    query = db.select(Role)
    roles = db.session.execute(query).scalars()
    return [
        {
            "id": role.id,
            "name": role.name
        }
        for role in roles
    ]
    
@bp.route('/', methods=['GET', 'POST'])
def handle_role():
    if request.method == 'POST':
        create_role()
        return {"msg": "Role created"}, HTTPStatus.CREATED
    else:
        return {"Roles": _list_roles()}, HTTPStatus.OK