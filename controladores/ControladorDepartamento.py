from Modelos.Departamento import Departamento
from Repositorios.DepartamentoRepositorio import DepartamentoRepositorio

class ControladorDepartamento():
    def __init__(self):                         # --init  constructor del controlador
        print("...Creando ControladorDepartamento")
        self.repositorio = DepartamentoRepositorio()

    def index(self):
        print("Listar todos los Departamentos")
        x = self.repositorio.findAll()
        return x
    """
        unDepartamento={
        "_id":"abc123",
        "nombre":"Medicina",
        "descripcion":"Departamento de medicina y salud"
        }
        return [unDepartamento]
    """
    def create(self,data):
        print("Crear un estudiante")
        elDepartamento = self.repositorio.save(Departamento(data))
        return elDepartamento

    def show(self,id):
        print("Mostrando un departamento con id ",id)
        elDepartamento = self.repositorio.findById(id)
        return elDepartamento
    """    
        elDepartamento = {
        "_id": id,
        "nombre":"Medicina",
        "descripcion":"Departamento de medicina y salud"
        }
        return elDepartamento
    """
    def update(self,id,data):
        print("Actualizando departamento con id ",id)
        departamentoActual=Departamento(self.repositorio.findById(id))
        departamentoActual.nombre      = data["nombre"]
        departamentoActual.descripcion = data["descripcion"]
        
        return self.repositorio.save(departamentoActual)
        

    def delete(self,id):
        print("Eliminando Departamento con id ",id)
        return  self.repositorio.delete(id)
        