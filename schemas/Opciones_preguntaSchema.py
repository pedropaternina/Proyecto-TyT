from db import ma
from models import Opciones_pregunta
from marshmallow_sqlalchemy.fields import Nested

class Opciones_preguntaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Opciones_pregunta
    
    id = ma.auto_field(dump_only=True)
    id_preguntas = ma.auto_field()
    texto_opcion = ma.auto_field()
    es_correcta = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
    
    preguntas = Nested("PreguntasSchema", dump_only=True)
    