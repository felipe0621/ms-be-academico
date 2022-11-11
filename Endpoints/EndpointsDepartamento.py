from flask import jsonify, Blueprint, make_response, request
from Controladores.ControladorDepartamento   import ControladorDepartamento
import endpoints

controladorDepartamento = ControladorDepartamento()

endpointDepartamento = Blueprint('endpointsDepartamento',__name__)

#################################################################
#Endpoints para modelo Departamento

@endpointDepartamento.route("/departamento",methods=['GET'])    #para listar todos los Departamentos
def index():
    json=controladorDepartamento.index()
    return jsonify(json)

@endpointDepartamento.route("/departamento/<string:id>",methods=['GET']) # para listar un solo departamento
def retrieve(id):
    json=controladorDepartamento.show(id)
    return jsonify(json)

@endpointDepartamento.route("/departamento",methods=['POST'])
def create():
    data = request.get_json()
    json=controladorDepartamento.create(data)
    return jsonify(json)

@endpointDepartamento.route("/departamento/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json=controladorDepartamento.update(id, data)
    return jsonify(json)

@endpointDepartamento.route("/departamento/<string:id>",methods=['DELETE'])
def delete(id):
    json=controladorDepartamento.delete(id)
    return jsonify(json)