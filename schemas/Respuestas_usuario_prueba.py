from db import ma
from models import Respuestas_usuario_prueba
from marshmallow_sqlalchemy.fields import Nested

class Respuestas_usuario_pruebaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Respuestas_usuario_prueba

    id = ma.auto_field(dump_only=True)
    id_pruebas = ma.auto_field()
    id_preguntas = ma.auto_field()
    id_opciones_pregunta = ma.auto_field()
    es_correcta = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)

    pruebas = Nested("PruebasSchema", dump_only=True)
    preguntas = Nested("PreguntasSchema", dump_only=True)
    opciones_pregunta = Nested("Opciones_preguntaSchema", dump_only=True)
    