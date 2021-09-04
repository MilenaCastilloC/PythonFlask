from flask import request
from flask_restful import Resource,Api
from flask import Flask
from typing import Dict
from flask import Flask


def create_app(config_dict: Dict = {}):
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f'sqlite:///{config_dict.get("DATABASE", "clinicaABC")}.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "frase-secreta"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["TESTING"] = config_dict.get("TESTING", False)
    return app

class VistaUsuario(Resource):
    def post(self, id_usuario):       
        request.json["id_usuario"]=id_usuario;
        return request.json

    def get(self, id_usuario):
        data={
            "nombre" : "Alberto",
            "contrasena" : "Perez",
            "id" : id_usuario
        }
        return data



app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaUsuario, "/usuario/<int:id_usuario>")


if __name__ == '__main__':
    app.run()