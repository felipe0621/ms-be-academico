from flask import jsonify, Blueprint, make_response, request
from Controladores.ControladorEstudiante import ControladorEstudiante
import endpoints

controladorEstudiante = ControladorEstudiante()

endpointEstudiante = Blueprint('endpointsEstudiante',__name__)

#################################################################
#Endpoints para modelo estudiante

@endpointEstudiante.route("/estudiante",methods=['GET'])    #para listar todos los estudiantes
def index():
    json=controladorEstudiante.index()
    return jsonify(json)

@endpointEstudiante.route("/estudiante/<string:id>",methods=['GET']) # para listar un solo estudiante
def retrieve(id):
    json=controladorEstudiante.retrieve(id)
    return jsonify(json)

@endpointEstudiante.route("/estudiante",methods=['POST'])
def create():
    data = request.get_json()
    json=controladorEstudiante.create(data)
    return jsonify(json)

@endpointEstudiante.route("/estudiante/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json=controladorEstudiante.update(id, data)
    return jsonify(json)

@endpointEstudiante.route("/estudiante/<string:id>",methods=['DELETE'])
def delete(id):
    json=controladorEstudiante.delete(id)
    return jsonify(json)