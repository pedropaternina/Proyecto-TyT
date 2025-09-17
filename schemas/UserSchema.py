from db import ma
from models import Users

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Users
        load_instance = True
    
    id = ma.auto_field(dump_only=True)
    nombres = ma.auto_field()
    apellidos = ma.auto_field()
    correo = ma.auto_field()
    password = ma.auto_field(load_only= True)
    created_at = ma.auto_field(dump_only=True)

    