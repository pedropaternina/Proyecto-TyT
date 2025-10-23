from schemas.PruebasSchema import PruebasSchema
from models.Pruebas import Pruebas
from db import db


def get_Pruebas():
    schema = PruebasSchema(many=True)
    prueba_consulta = Pruebas.query.order_by("id").all()
    return schema.dump(prueba_consulta)

def get_Prueba_Id(id_prueba):
    schema = PruebasSchema()
    prueba_consulta = Pruebas.query.filter_by(id=id_prueba).first()

    if not prueba_consulta:
        return {"Error": "La prueba no se ha realizado"}
    
    return schema.dump(prueba_consulta)

def get_Prueba_Tematica_Usuario(id_tematica, usuario):
    schema = PruebasSchema()
    prueba_consulta = Pruebas.query.filter_by(id_tematica=id_tematica, id_usuario=usuario).all()

    if not prueba_consulta:
        return {"Error": "No se encontro pruebas para esas especificaciones"}
    
    return schema.dump(prueba_consulta)

def add_Pruebas(data: dict):
    schema = PruebasSchema()
    prueba_data = schema.load(data)
    prueba = Pruebas(**prueba_data)


    # Realmente pueden haber dos pruebas iguales, no hay mucha razon para meditar esto

    db.session.add(prueba)
    db.session.commit()

    return schema.dump(prueba)

def deletePruebas(prueba):
    prueba_consulta = Pruebas.query.filter_by(id=prueba)

    if not prueba_consulta:
        return {"Error": "No se encontro la prueba"}, 404
    
    db.session.delete(prueba_consulta)
    db.session.commit()
    return 'Prueba eliminada con exito'