
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import json
import endpoints

from Controladores.ControladorEstudiante import ControladorEstudiante


app = Flask(__name__)

#Permite a un servidor hacer peticiones de diferentes varios dominios distintos
cors = CORS(app)


#se importan las rutas de estudiante en el main
#app.register_blueprint(endpoints.endpointEstudiante)

controladorEstudiante = None

def __loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running .Pruebas pipe.."
    return jsonify(json)

@app.route("/estudiante",methods=['GET'])
def index():
    pass
@app.route("/estudiante/<string:id>",methods=['GET'])
def retrieve():
    pass
@app.route("/estudiante",methods=['POST'])
def create():
    pass
@app.route("/estudiante/<string:id>",methods=['PUT'])
def update():
    pass
@app.route("/estudiante/<string:id>",methods=['DELETE'])
def delete():
    pass

if __name__=='__main__':
    dataConfig = __loadFileConfig()
    print("Server running  : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
     

     #Para hacer una prueba de conexión
    if dataConfig["test"] == "true":
        print("Testing DB conecction...")
        from Repositorios.InterfaceRepositorio import InterfaceRepositorio
        repo = InterfaceRepositorio()
    else:
        controladorEstudiante = ControladorEstudiante()
        serve(app,host=dataConfig["url-backend"],port=dataConfig["port"]) #production -grade WSGI server
      