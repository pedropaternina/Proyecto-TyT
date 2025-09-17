from flask import Flask
from config import Config
from db import db, migrate
from routes.users_routes import users_bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(users_bp, url_prefix="/users")


    return app





if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)