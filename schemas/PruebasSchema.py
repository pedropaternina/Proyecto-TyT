from db import ma
from models import Pruebas
from marshmallow_sqlalchemy.fields import Nested

class PruebasSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pruebas

    id = ma.auto_field(dump_only=True)
    id_usuario = ma.auto_field()
    id_tematicas = ma.auto_field()
    puntuacion = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)

    users =  Nested("UserSchema", dump_only=True)
    tematicas = Nested("TematicasSchema", dump_only=True)