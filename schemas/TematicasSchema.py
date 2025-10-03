from db import ma
from models import Tematicas
from marshmallow import fields, Schema

class TematicasSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tematicas

    id = ma.auto_field(dump_only=True)
    nombre_tematica = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)


class UpdateSchema(Schema):
    class Meta:
        field = ("nombre_tematica")
    
    nombre_tematica = fields.Str(required=False)