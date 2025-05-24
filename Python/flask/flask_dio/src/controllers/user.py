from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import inspect
from src.app import User, db
from http import HTTPStatus

bp = Blueprint('user', __name__, url_prefix='/users') #em restful apps, os modulos sao sempre no plural

def _create_user(): 
    data = request.json
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        for user in users
    ], HTTPStatus.OK


@bp.route('/', methods=['GET', 'POST'])
@jwt_required()
def handle_user():
    if request.method == 'POST':
        _create_user()
        return {"message": "User created!"}, HTTPStatus.CREATED #retorna o status de documento criado na api (201)
    else:
        return {"Users": _list_users()}
    

@bp.route('/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "User": user.username,
        "Email": user.email
    }, HTTPStatus.OK #retorna o status ok (200)


@bp.route('/<int:user_id>/update', methods=['PATCH'])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json #request json retorna um dicionário, podendo os dados serem acessados com 'username'
    
    mapper = inspect(User) #com inspect o codigo do PATCH fica mais dinamico.
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    return [
        {
            "User": user.username,
            "Email": user.email
        }
    ], HTTPStatus.OK

@bp.route('/<int:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT #NO_CONTENT indica que foi realizada a operacao e nao tem nada a retornar, 204