from flask import request
from flask_restful import Resource,Api
from flask import Flask
from typing import Dict
from flask import Flask
import random

def create_app(config_dict: Dict = {}):
    app = Flask(__name__)    
    return app

class VistaPaciente(Resource):
    def post(self, id_paciente):       
        data={
            "id" : id_paciente,
            "nombre" : request.json["nombre"],
            "documento" : request.json["documento"]
        }
        return request.json
        return data

    def get(self, id_paciente):
        data={
            "id" : id_paciente,
            "nombre" : random.randbytes(30),
            "documento" : random.randint(100, 999)
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