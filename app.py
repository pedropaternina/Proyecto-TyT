from flask import Flask
from config import Config
from db import db, migrate, ma, jwt
from routes.users_routes import users_bp 
from routes.preguntas_routes import preguntas_bp
from routes.tematicas_routes import tematicas_bp
from routes.opciones_pregunta_routes import opciones_preguntas_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    
        


    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(preguntas_bp, url_prefix="/preguntas")
    app.register_blueprint(tematicas_bp, url_prefix="/tematicas")
    app.register_blueprint(opciones_preguntas_bp, url_prefix="/opciones_preguntas")

    return app





if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)