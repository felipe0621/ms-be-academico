
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import json
import Endpoints


from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorMateria import ControladorMateria
miControladorEstudiante=ControladorEstudiante()
miControladorDepartamento=ControladorDepartamento()
miControladorMateria=ControladorMateria()

app = Flask(__name__)

#Permite a un servidor hacer peticiones de diferentes varios dominios distintos
cors = CORS(app)


#se importan las rutas de estudiante en el main
app.register_blueprint(Endpoints.endpointEstudiante)
app.register_blueprint(Endpoints.endpointDepartamento)
app.register_blueprint(Endpoints.endpointMateria)

def __loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

#PARA PRUEBA
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running .Pruebas pipe.."
    return jsonify(json)




if __name__=='__main__':
    dataConfig = __loadFileConfig()
    print("Server running  : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
     

     #Para hacer una prueba de conexión
    if dataConfig["test"] == "true":
        print("Testing DB conecction...")
        from Repositorios.InterfaceRepositorio import InterfaceRepositorio
        repo = InterfaceRepositorio()
    else:
        serve(app,host=dataConfig["url-backend"],port=dataConfig["port"]) #production -grade WSGI server
      
@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    json=miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(json)