from db import ma
from models import Preguntas
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import Schema, fields


class PreguntasSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Preguntas
    
    id = ma.auto_field(dump_only=True)
    id_tematicas = ma.auto_field()
    context = ma.auto_field()
    context_img = ma.auto_field()
    enunciado = ma.auto_field()
    created_at = ma.auto_field(dump_only=True) 

    tematicas = Nested("TematicasSchema", dump_only=True)


class UpdatePreguntasSchema(Schema):
    class Meta:
        fields = ("contex","context_img","enunciado")

    context = fields.Str(required=False)
    context_img = fields.Str(required=False),
    enunciado = fields.Str(required=False)