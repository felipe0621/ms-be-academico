from Modelos.Inscripcion import Inscripcion
class ControladorInscripcion():
    def __init__(self):                         # --init  constructor del controlador
        print("...Creando ControladorInscripcion")

    def index(self):
        print("Listar todas las Inscripciones")
        unaInscripcion={
        "_id":"4521",
        "año":"2020",
        "semestre":"2",
        "notaFinal":"3.8"
        }
        return [unaInscripcion]

    def create(self,infoInscripcion):
        print("Crear una inscripción")
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def show(self,id):
        print("Mostrando una materia con id ",id)
        laInscripcion = {
        "_id":"4521",
        "año":"2020",
        "semestre":"2",
        "notaFinal":"3.8"
        }
        return laInscripcion

    def update(self,id,infoInscripcion):
        print("Actualizando inscripción con id ",id)
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def delete(self,id):
        print("Elimiando Inscripción con id ",id)
        return {"deleted_count":1}