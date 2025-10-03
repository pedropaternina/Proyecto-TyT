from schemas.TematicasSchema import TematicasSchema, UpdateSchema
from models.Tematicas import Tematicas
from db import db


def create_Tematicas(data: dict):
    schema = TematicasSchema()
    tematica_data = schema.load(data)
    tematica = Tematicas(**tematica_data)
    
    tematica_consulta = Tematicas.query.filter_by(nombre_tematica=tematica_data["nombre_tematica"]).first()

    if tematica_consulta:
        return {"error": "Tematica ya existe"}, 404
    
    

    db.session.add(tematica)
    db.session.commit()

    return schema.dump(tematica)



def get_Tematicas():
    schema = TematicasSchema(many=True)
    tematica_consulta = Tematicas.query.order_by("id").all()
    return schema.dump(tematica_consulta)


def get_Tematica_Id(id_tematica):
    schema = TematicasSchema()
    tematica_consulta = Tematicas.query.filter_by(id=id_tematica).first()

    if not tematica_consulta:
        return {"error": "La tematica no existe"}, 404
    
    return schema.dump(tematica_consulta)

def update_Tematica_Id(data: dict, id_tematica):
    schema = UpdateSchema()
    tematica_update = schema.load(data)
    tematica_consulta = Tematicas.query.filter_by(id=id_tematica).first()

    if not tematica_consulta:
        return {"error":"La tematica no existe"}, 404
    
    for key, value in tematica_update.items():
        setattr(tematica_consulta, key, value)

    db.session.commit()
    tematica_schema = TematicasSchema()
    return tematica_schema.dump(tematica_update)

def delete_Tematica_Id(id_tematica):
    tematica_consulta = Tematicas.query.filter_by(id=id_tematica).first()

    if not tematica_consulta:
        return {"error": "Tematica no existe"}
    
    db.session.delete(tematica_consulta)
    db.session.commit()

    return f"La temaica {tematica_consulta.nombre_tematica} con el id {tematica_consulta.id} fue eliminada exitosamente"