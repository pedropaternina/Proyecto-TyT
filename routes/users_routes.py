from flask import Blueprint, request
from service.auth_service import crear_usuario
users_bp = Blueprint("users",__name__)

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return crear_usuario(data)