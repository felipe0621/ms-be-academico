from Repositorios.MateriaRepositorio import MateriaRepositorio
from Repositorios.DepartamentoRepositorio import DepartamentoRepositorio
from Modelos.Materia import Materia
from Modelos.Departamento import Departamento


class ControladorMateria():
    
        
    def __init__(self):                         # --init  constructor del controlador
        print("...Creando ControladorMateria")
        self.repositorio= MateriaRepositorio()
        self.repositorioDepartamento = DepartamentoRepositorio()

    def index(self):
        print("...Listar todas las Materias")
        x = self.repositorio.findAll()
        return x
        
    """
        unaMateria={
        "_id":"4521",
        "nombre":"Programación 1",
        "creditos":"256"
        }
        return [unaMateria]        
    """
    
    def create(self,data):
        print("Crear una materia")
        laMateria = self.repositorio.save(Materia(data))
        return laMateria

    def show(self,id):
        print("Mostrando una materia con id ",id)
        laMateria = self.repositorio.findById(id)
        return laMateria
        
    """
        laMateria = {
        "_id": id,
        "nombre":"Programación 1",
        "creditos":"256"
        }
        return laMateria
    """
    def update(self,id,data):
        print("Actualizando materia con id ",id)
        materiaActual=Materia(self.repositorio.findById(id))
        materiaActual.nombre     = data["nombre"]
        materiaActual.creditos   = data["creditos"]
        
        return self.repositorio.save(materiaActual)
        
               

    def delete(self,id):
        print("Elimiando Materia con id ",id)
        return  self.repositorio.delete(id)
        
       
    """
    Relación departamento y materia
    """
    def asignarDepartamento(self,id,id_departamento):
        materiaActual=Materia(self.repositorio.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento=departamentoActual
        return self.repositorio.save(materiaActual)
  
  
  
   