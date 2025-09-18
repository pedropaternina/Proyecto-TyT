from flask import Blueprint, request
from service.auth_service import crear_usuario, login_user
from service.users_service import get_Usuarios, get_Usuario_Id, delete_User_By_Id, update_Usuario_By_Id
users_bp = Blueprint("users",__name__)

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return crear_usuario(data)

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return login_user(data)

@users_bp.route("/", methods=["GET"])
def get_Users():
    return get_Usuarios()

@users_bp.route("/<int:id>", methods=["GET"])
def get_user_by_id(id):
    return get_Usuario_Id(id)

@users_bp.route("/update/<int:id>", methods=["POST"]) 
def update_user_by_id(id):
    data = request.get_json()
    return update_Usuario_By_Id(data, id)

@users_bp.route("/delete/<int:id>", methods=["DELETE", "POST", "GET"])
def delete_user_by_id(id):
    return delete_User_By_Id(id)