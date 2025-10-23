from flask import Blueprint, request
from service.opciones_preguntas_service import get_Opreguntas,add_Opreguntas , get_Opreguntas_Id, get_Opreguntas_Idpregunta , update_Opreguntas, delete_Opreguntas


opciones_preguntas_bp = Blueprint("opciones_preguntas",__name__)

@opciones_preguntas_bp.route("/", methods=["GET"])
def obtener_opreguntas():
    return get_Opreguntas()

@opciones_preguntas_bp.route("/add", methods=["POST"])
def add_opreguntas():
    data = request.get_json()
    return add_Opreguntas(data)


@opciones_preguntas_bp.route("/<int:id_opreguntas>", methods=["GET"])
def obtener_opreguntas_id(id_opreguntas):
    return get_Opreguntas_Id(id_opreguntas)

@opciones_preguntas_bp.route("/preguntas/<int:id_pregunta>", methods=["GET"])
def obtener_oppregunta_preguna(id_pregunta):
    return get_Opreguntas_Idpregunta(id_pregunta)

@opciones_preguntas_bp.route("/update/<int:id_opreguntas>", methods=["POST"])
def update_opreguntas(id_opreguntas):
    data = request.get_json()
    return update_Opreguntas(data, id_opreguntas)

@opciones_preguntas_bp.route("/delete/<int:id_opreguntas>", methods=["DELETE"])
def delete_opreguntas(id_opreguntas):
    return delete_Opreguntas(id_opreguntas)