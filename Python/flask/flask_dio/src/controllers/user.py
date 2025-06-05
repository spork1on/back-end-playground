from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import inspect
from src.app import User, db
from http import HTTPStatus
from werkzeug.security import generate_password_hash

bp = Blueprint('user', __name__, url_prefix='/users') #em restful apps, os modulos sao sempre no plural

def _create_user(): 
    data = request.json
    user = User(
        username=data["username"], 
        email=data["email"], 
        password=generate_password_hash(data["password"]),
        role_id=data["role_id"]
    )
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role_id": user.role_id
        }
        for user in users
    ]


@bp.route('/', methods=['GET', 'POST'])
@jwt_required()
def handle_user():
    identity = get_jwt_identity()
    usr = db.session.scalar(db.select(User).where(User.username == identity))
    isadmin = identity == 'dev' or (usr and usr.role_id == 1)

    if not isadmin:
        return {"msg": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
    

    if request.method == 'POST':
        _create_user()
        return {"message": "User created!"}, HTTPStatus.CREATED #retorna o status de documento criado na api (201)
        
    return {"Users": _list_users()}, HTTPStatus.OK
    
    
@bp.route('/<int:user_id>')
@jwt_required()
def get_user(user_id):
    identity = get_jwt_identity()
    usr = db.session.scalar(db.select(User).where(User.username == identity))
    user = db.get_or_404(User, user_id)
    isadmin = identity == 'dev' or (usr and usr.role_id == 1)

    if not isadmin and usr.id != user_id:
        return {"msg": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    return {
        "User": user.username,
        "Email": user.email
    }, HTTPStatus.OK #retorna o status ok (200)


@bp.route('/<int:user_id>/update', methods=['PATCH'])
@jwt_required()
def update_user(user_id):
    identity = get_jwt_identity()
    auth_user = db.session.scalar(db.select(User).where(User.username == identity))
    target_usr = db.get_or_404(User, user_id)
    data = request.json #request json retorna um dicionário, podendo os dados serem acessados com 'username'
    
    isadmin = identity == 'dev' or (auth_user and auth_user.role_id == 1)
    
    if not isadmin and auth_user.id != user_id:
        return {"msg": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
    
    mapper = inspect(User) #com inspect o codigo do PATCH fica mais dinamico.
    for column in mapper.attrs:
        if column.key in data:
            setattr(target_usr, column.key, data[column.key])
    db.session.commit()
    
    return [
        {
            "User": target_usr.username,
            "Email": target_usr.email
        }
    ], HTTPStatus.OK


@bp.route('/<int:user_id>/delete', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    identity = get_jwt_identity()
    auth_user = db.session.scalar(db.select(User).where(User.username == identity))
    target_usr = db.get_or_404(User, user_id)
    isadmin = identity == 'dev'or (auth_user and auth_user.role_id == 1)

    if not isadmin and auth_user != target_usr.id:
        return {"msg": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

    db.session.delete(target_usr)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT #NO_CONTENT indica que foi realizada a operacao e nao tem nada a retornar, 204

@bp.route('/register', methods=['POST']) #public route for user common user creation
def user_register():    
    data = request.json
    user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role_id=0
    )
    db.session.add(user)
    db.session.commit()

    return {"msg": "Conta criada com sucesso"}, HTTPStatus.CREATED