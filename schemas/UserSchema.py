from db import ma
from models.Users import Users
from dataclasses import dataclass
from marshmallow import fields, Schema
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



class LoginSchema(Schema):
    class Meta:
        fields = ("correo","password")
    correo = fields.Str()
    password = fields.Str()

class UpdateSchema(Schema):
    class Meta:
        fields = ("nombres","apellidos","correo","password")

    nombres = fields.Str(required=False)
    apellidos = fields.Str(required=False)
    correo = fields.Str(required=False)
    password = fields.Str(required=False)

