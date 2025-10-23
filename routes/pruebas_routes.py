from flask import Blueprint, request
from service.prueba_service import get_Prueba_Id, get_Prueba_Tematica_Usuario ,get_Pruebas, add_Pruebas, deletePruebas

pruebas_bp = Blueprint("pruebas", __name__)

@pruebas_bp.route("/", methods=["GET"])
def obtener_pruebas():
    return get_Pruebas()

@pruebas_bp.route("/<int:id_prueba>")
def obtener_prueba_id(id_prueba):
    return get_Prueba_Id(id_prueba)

@pruebas_bp.route("/<int:id_tematica>/<int:id_usuario>", methods=["GET"])
def obtener_prueba_idtematica_idusuario(id_tematica, id_usuario):
    return get_Prueba_Tematica_Usuario(id_tematica, id_usuario)


@pruebas_bp.route("/", methods=['POST'])
def createPrueba():
    data = request.get_json()
    return add_Pruebas(data)

@pruebas_bp.route("/<int:id_prueba>", methods=['DELETE'])
def eliminar_pruebas(id_prueba):
    return eliminar_pruebas(id_prueba)