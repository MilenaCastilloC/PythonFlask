from flask import request
from flask_restful import Resource,Api
from flask import Flask
from typing import Dict
from flask import Flask


def create_app(config_dict: Dict = {}):
    app = Flask(__name__)    
    return app

class VistaPaciente(Resource):
    def post(self, id_paciente):       
        request.json["id_usuario"]=id_paciente;
        return request.json

    def get(self, id_paciente):
        data={
            "nombre" : "Alberto",
            "contrasena" : "Perez",
            "id" : id_paciente
        }
        return data

class HealthCheck(Resource):    

    def get(self):
        data={
            "echo" : "ok"
        }
        return data



app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaPaciente, "/paciente/<int:id_paciente>")
api.add_resource(HealthCheck, "/paciente/healtchek")


if __name__ == '__main__':
    app.run()