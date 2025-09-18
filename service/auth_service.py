from db import db
from utils.encrypt import hash_password, check_password
from schemas.UserSchema import UserSchema, LoginSchema
from models.Users import Users
from flask_jwt_extended import create_access_token
from flask import jsonify

def crear_usuario(data: dict):
    schema = UserSchema()
    user = schema.load(data) # type: ignore
    users_consulta = Users.query.filter_by(correo=user.correo).first()
    
    if users_consulta:
        return {"error": "Usuario ya existe"}, 400

    user.password = hash_password(user.password)
    
    db.session.add(user)
    db.session.commit()

    return schema.dump(user) # type: ignore


def login_user(data: dict):
    schema = LoginSchema()
    user = schema.load(data)
    users_consulta = Users.query.filter_by(correo=user["correo"]).first()

    if users_consulta == None:
        return {"error": "Usuario no existe"}, 400
    
    if check_password(user["password"], users_consulta.password):
        access_token = create_access_token(identity=user["correo"])
        return jsonify(access_token=access_token)

        
