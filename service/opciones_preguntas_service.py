from models.Opciones_pregunta import Opciones_pregunta
from schemas.Opciones_preguntaSchema import Opciones_preguntaSchema, Update_opciones_preguntaSchema
from db import db

def get_Opreguntas():
    schema = Opciones_preguntaSchema(many=True)
    op_consulta = Opciones_pregunta.query.order_by("id").all()

    return schema.dump(op_consulta)

def get_Opreguntas_Id(id_opreguntas):
    schema = Opciones_preguntaSchema()
    op_consulta = Opciones_pregunta.query.filter_by(id=id_opreguntas).first()

    if not op_consulta():
        return {"error": "La opcion de pregunta no fue encontrada"}
    
    return schema.dump(op_consulta)

def add_Opreguntas(data:dict):
    schema = Opciones_preguntaSchema()
    op_pregunta_data = schema.dump()
    op_pregunta = Opciones_pregunta(**op_pregunta_data)

    op_consulta = Opciones_pregunta.query.filter_by(id_preguntas = op_pregunta.id_preguntas, texto_opcion=op_pregunta.texto_opcion )

    if op_pregunta:
        return {"error": "Ya exise una opcion de pregunta con esas caracteristicas"}
    
    db.session.add(op_pregunta)
    db.session.commit()

    return schema.dump(op_pregunta)


def update_Opreguntas(data: dict, id_opregunta):
    schema = Update_opciones_preguntaSchema()
    op_update = schema.dump(data)
    op_consulta = Opciones_pregunta.query.filter_by(id=id_opregunta).first()

    if not op_consulta:
        return {"Error": "La Opcion de pregunta no existe"}
    
    for key, value in op_update.items():
        setattr(op_consulta, key, value )

    db.session.commit()
    op_schema = Opciones_preguntaSchema()
    return op_schema.dump(op_consulta)
