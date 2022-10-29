from abc import ABCMeta   #superclase esta no puede instanciar

class AbstractModelo(metaclass=ABCMeta):
    def __init__(self,data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
            
            
            
#otro comentario en el interface