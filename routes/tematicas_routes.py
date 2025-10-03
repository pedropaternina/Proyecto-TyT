from flask import Blueprint, request
from service.tematicas_service import get_Tematica_Id, get_Tematicas, update_Tematica_Id, delete_Tematica_Id, create_Tematicas

tematicas_bp = Blueprint("tematicas",__name__)

@tematicas_bp.route("/", methods=["GET"])
def get_tematicas():
    return get_Tematicas()

@tematicas_bp.route("/add", methods=["POST"])
def add_tematicas():
    data = request.get_json()
    return create_Tematicas(data)

@tematicas_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    return get_Tematica_Id(id)

@tematicas_bp.route("/update/<int:id>", methods=["POST"])
def update_by_id(id):
    data = request.get_json()
    return update_Tematica_Id(data, id)

@tematicas_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    return delete_Tematica_Id(id)
