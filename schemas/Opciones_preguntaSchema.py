from db import ma
from models import Opciones_pregunta
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import fields, Schema

class Opciones_preguntaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Opciones_pregunta
    
    id = ma.auto_field(dump_only=True)
    id_preguntas = ma.auto_field()
    texto_opcion = ma.auto_field()
    es_correcta = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
    
    preguntas = Nested("PreguntasSchema", dump_only=True)
    


class Update_opciones_preguntaSchema(Schema):
    class Meta:
        fields = ("id_preguntas", "texto_opcion", "es_correcta")

    id_preguntas = fields.Int(required=False)
    texto_opcion = fields.Str(required=False)
    es_correcta = fields.Bool(required=False)