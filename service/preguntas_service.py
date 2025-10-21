from schemas.PreguntasSchema import PreguntasSchema, UpdatePreguntasSchema
from models.Preguntas import Preguntas
from db import db


# En pausa por creacion de tematicas 

def get_Preguntas():
    schema = PreguntasSchema(many=True)
    pregunta_consulta = Preguntas.query.order_by("id").all()
    return schema.dump(pregunta_consulta)

def get_Pregunta_Id(id_pregunta):
    schema = PreguntasSchema()
    pregunta_consulta = Preguntas.query.filter_by(id=id_pregunta)

    if not pregunta_consulta:
        return {"error":"La pregunta no existe"}
    
    return schema.dump(pregunta_consulta)

def get_Pregunta_Tematica(id_tematica):
    schema = PreguntasSchema(many=True)
    pregunta_consula = Preguntas.query.filter_by(id_tematicas=id_tematica).all()

    if not pregunta_consula:
        return {"Error": "Las preguntas no existen"}
    
    return schema.dump(pregunta_consula)


def add_Preguntas(data: dict):
    schema = PreguntasSchema()
    pregunta_data = schema.load(data) 
    pregunta = Preguntas(**pregunta_data)
   
   # esto podria ser temporal, no considero que sea la mejor forma de evitar que
   # se dupliquen preguntas, pero para testear
    pregunta_consulta = Preguntas.query.filter_by(context=pregunta.context, enunciado=pregunta.enunciado).first()

    if pregunta_consulta:
        return {"error": "Ya existe una pregunta con ese mismo contexto o enunciado"} , 404


    db.session.add(pregunta)
    db.session.commit()

    return schema.dump(pregunta)


def updatePreguntas(data: dict, id_pregunta):
    schema = UpdatePreguntasSchema()
    pregunta_update = schema.load(data)
    pregunta_consulta = Preguntas.query.filter_by(id = id_pregunta).first()

    if not pregunta_consulta:
        return {"error":"La pregunta con ese Id no existe"}, 404
    
    for key, value in pregunta_update.items():
        setattr(pregunta_consulta,key,value)

    db.session.commit()
    
    pregunta_schema = PreguntasSchema()
    return pregunta_schema.dump(pregunta_consulta)


def deletePreguntas(id_pregunta):
    pregunta_consulta = Preguntas.query.filter_by(id=id_pregunta).first()

    if not pregunta_consulta:
        return {"error": "La pregunta no existe o ya fue eliminada con exito"}, 404
    
    db.session.delete(pregunta_consulta)
    db.session.commit()
    return f"La pregunta con el id: {id_pregunta} ha sido eliminada exitosamente"
