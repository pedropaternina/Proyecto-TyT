from db import db
from utils.encrypt import hash_password
from schemas.UserSchema import UserSchema 
from models.Users import Users

def crear_usuario(data: dict):
    schema = UserSchema
    user = Users = schema.load(data) # type: ignore
    users_consulta = Users.query.filter_by(correo=user.correo).first()
    
    if users_consulta:
        return {"error": "Usuario ya existe"}, 400

    user.password = hash_password(user.password)
    
    db.session.add(user)
    db.session.commit()

    return schema.dump(user) # type: ignore