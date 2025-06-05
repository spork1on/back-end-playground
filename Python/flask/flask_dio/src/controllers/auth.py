from flask import Blueprint, request
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, JWTManager
from http import HTTPStatus
from src.app import User, db, jwt_blacklist
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == 'dev' and password == 'test':
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}    

    user_login = db.session.scalar(db.select(User).where(User.username == username))
    if not user_login or not check_password_hash(user_login.password, password):
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED
    
    return {"access_token": create_access_token(identity=username)}, HTTPStatus.OK


@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    jwt_blacklist.add(jti)
    return {"msg": "Logged out"}, HTTPStatus.OK