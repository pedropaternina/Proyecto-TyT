from flask import Blueprint, request 
from service.preguntas_service import get_Preguntas, add_Preguntas, get_Pregunta_Id, get_Pregunta_Tematica, updatePreguntas, deletePreguntas

preguntas_bp = Blueprint("preguntas",__name__)

@preguntas_bp.route("/", methods=['GET'])
def obtener_preguntas():
    return get_Preguntas()

@preguntas_bp.route("/",methods=['POST'])
def add_preguntas():
    data = request.get_json()
    return add_Preguntas(data)

@preguntas_bp.route("/<int:id_pregunta>", methods=["GET"])
def obtener_preguntas_id(id_pregunta):
    return get_Pregunta_Id(id_pregunta)


@preguntas_bp.route("/tematica/<int:id_tematica>", methods=["GET"])
def obtener_preguntas_tematica(id_tematica):
    return get_Pregunta_Tematica(id_tematica)

@preguntas_bp.route("/update/<int:id_pregunta>", methods=["POST"])
def update_preguntas(id_pregunta):
    data = request.get_json()
    return updatePreguntas(data, id_pregunta)

@preguntas_bp.route("/delete/<int:id_pregunta>", methods=["DELETE"])
def delete_preguntas(id_pregunta):
    return deletePreguntas(id_pregunta)
