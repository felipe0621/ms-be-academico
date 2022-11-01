
from Modelos.Estudiante import Estudiante
from Repositorios.EstudianteRepositorio import EstudianteRepositorio


#Clase que implementa el controlador para los endpoints relacionados con estudiante
class ControladorEstudiante():
    def __init__(self):   #constructor   
        print(" >Creando ControladorEstudiante")
        self.repositorio = EstudianteRepositorio() #segun video tutoria grupal
        #self.EstudianteRepositorio = EstudianteRepositorio()#segun la guia

        # Funcion para listar todos los estudiantes
    def index(self):
        print(" >Listar todos los estudiantes")
        x = self.repositorio.findAll()
       
        """
        unEstudiante = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        """        
        return x
      
        #return self.EstudianteRepositorio.findAll()

    # Funcion para crear un estudiante
    def create(self, data):  # ese data se refiere al json que se mando desde el postman
        print(" >Crear un estudiante")
        elEstudiante = self.repositorio.save(Estudiante(data))
        
        return elEstudiante.__dict__     #retorna el estudiante en formato json con la mismao infor
        #nuevoEstudiante=Estudiante(infoEstudiante)
        #return self.EstudianteRepositorio.save(nuevoEstudiante)

    # Funcion para mostrar un estudiante por id
    def retrieve(self,id):   # en la guia aparece show
        print(" >Mostrando un estudiante con id ", id)
        elEstudiante = self.repositorio.findById(id)
        """
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
        """
        #elEstudiante=Estudiante(self.EstudianteRepositorio.findById(id))
        return elEstudiante

    # Funcion para actualizar un estudiante
    def update(self,id,data):
        print(" >Actualizando estudiante con id ", id)
        estudianteActual=Estudiante(self.EstudianteRepositorio.findById(id))
        estudianteActual.cedula   = data["cedula"]
        estudianteActual.nombre   = data["nombre"]
        estudianteActual.apellido = data["apellido"]
        return self.EstudianteRepositorio.save(estudianteActual)
    
    # Funcion para eliminar un estudiante
    def delete(self,id):
        print(" >Elimiando estudiante con id ", id)
        return  self.repositorio.delete(id)
        

