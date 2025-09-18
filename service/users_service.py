from schemas.UserSchema import UserSchema, UpdateSchema
from models.Users import Users
from db import db

def get_Usuarios():
    schema = UserSchema(many=True)
    users_consulta = Users.query.order_by("id").all()
    return schema.dump(users_consulta)


def get_Usuario_Id(id_user):
    schema = UserSchema()
    users_consulta = Users.query.filter_by(id=id_user).first()

    if not users_consulta:
        return {"error": "El usuario no existe"}, 404
    
    return schema.dump(users_consulta)

def update_Usuario_By_Id(data: dict,id_user):
    schema = UpdateSchema()
    user_update = schema.load(data)
    user_consulta = Users.query.filter_by(id=id_user).first()

    if not user_consulta:
        return {"error": "El usuario no existe"}, 404

    for key, value in user_update.items():
        setattr(user_consulta, key, value)
    
    db.session.commit()
    user_schema = UserSchema()
    return user_schema.dump(user_consulta)
    
    
    


def delete_User_By_Id(id):
    schema = UserSchema()
    user_consulta = Users.query.filter_by(id=id).first()

    if not user_consulta:
        return {"error": "El usuario no existe"}
    
    db.session.delete(user_consulta)
    db.session.commit()
    
    return f"Usuario con el id: {id} eliminado exitosamente"