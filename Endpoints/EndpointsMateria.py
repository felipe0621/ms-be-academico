from flask import jsonify, Blueprint, make_response, request
from Controladores.ControladorMateria import ControladorMateria
import endpoints

controladorMateria = ControladorMateria()

endpointMateria = Blueprint('endpointsMateria',__name__)

#################################################################
#Endpoints para modelo Materia

@endpointMateria.route("/materia",methods=['GET'])    #para listar todos los Materias
def index():
    json=controladorMateria.index()
    return jsonify(json)

@endpointMateria.route("/materia/<string:id>",methods=['GET']) # para listar un solo materia
def retrieve(id):
    json=controladorMateria.retrieve(id)
    return jsonify(json)

@endpointMateria.route("/materia",methods=['POST'])
def create():
    data = request.get_json()
    json=controladorMateria.create(data)
    return jsonify(json)

@endpointMateria.route("/materia/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json=controladorMateria.update(id, data)
    return jsonify(json)

@endpointMateria.route("/materia/<string:id>",methods=['DELETE'])
def delete(id):
    json=controladorMateria.delete(id)
    return jsonify(json)