from flask import jsonify, Blueprint, make_response, request
from Controladores.ControladorInscripcion import ControladorInscripcion
import endpoints

controladorInscripcion = ControladorInscripcion()

endpointInscripcion = Blueprint('endpointsInscripcion',__name__)

#################################################################
#Endpoints para modelo Inscripcion

@endpointInscripcion.route("/inscripcion",methods=['GET'])    #para listar todos los Inscripcions
def index():
    json=controladorInscripcion.index()
    return jsonify(json)

@endpointInscripcion.route("/inscripcion/<string:id>",methods=['GET']) # para listar un solo Inscripcion
def retrieve(id):
    json=controladorInscripcion.retrieve(id)
    return jsonify(json)

@endpointInscripcion.route("/inscripcion",methods=['POST'])
def create():
    data = request.get_json()
    json=controladorInscripcion.create(data)
    return jsonify(json)

@endpointInscripcion.route("/inscripcion/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json=controladorInscripcion.update(id, data)
    return jsonify(json)

@endpointInscripcion.route("/inscripcion/<string:id>",methods=['DELETE'])
def delete(id):
    json=controladorInscripcion.delete(id)
    return jsonify(json)