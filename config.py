import os

USER_DB = os.getenv("USER_DB","postgres")
USER_PASSWORD = os.getenv("USER_PASSWORD","Diavole27727")
SERVER_DB = os.getenv("SERVER_DB", "localhost")
NAME_DB = os.getenv("NAME_DB", "demo")

FULL_URL_DB = f"postgresql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}"

class Config:
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY","llave_secreta")