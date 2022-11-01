# esta parte se encarga de comunicarse con la base de datos MongoDB
#ORM para la base de datos MongoDB
#SU FUNCIONALIDAD esta intimamente ligada a la Api ofrecida por pymongo
#https://pymongo.readthedocs.io/en/stable/



import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_origin, get_args
import json

#comentario

T = TypeVar('T')

#https://realpython.com/documenting-python-code/
class InterfaceRepositorio(Generic[T]):
    """ORM PARA LA BASE DE DATOS MongoDB alojada en la plataforma atlas"""
    def __init__(self):     #CONSTRUCTOR
        ca = certifi.where()  #certificado para encriptar
        dataConfig = self.__loadFileConfig()  #para cargar el archivo de configuracion
        client = pymongo.MongoClient(dataConfig["mongo-db-connection-string"], tlsCAFile=ca) #para la conexion a bd
        self.baseDatos = client[dataConfig["name-db"]] 
        theClass = get_args(self.__orig_bases__[0])     #linea 27 y28 indica cual es el objeto que esta trabajando
        self.coleccion = theClass[0].__name__.lower()
        
        if dataConfig["test"] == "true":
            self.__test_dbConnection()
            
            #de la linea 22 a 31 es el constructor

    def __loadFileConfig(self):               #metodo para cargar archivos de configuracion
        with open('config.json') as f:
            data = json.load(f)
        with open('secrets.json') as f:            
            data.update(json.load(f))     
        return data

    def __test_dbConnection(self):                          #metodos para hacer las pruebas
        colecciones = self.baseDatos.list_collection_names()
        print(colecciones)
            # Explorando las colecciones
        for c in colecciones:
            print("coleccion:", c)
            print("   Campos:", end=" ")
            cursor = self.baseDatos[c].find({})
              #for document in cursor:
            try:
                    #print("  ", end="")
                print(cursor[0].keys())  #print all fields of this document
            except:
                print("Colección vacía")
                print("")                
              
    
    def save(self, item: T): #la T va a ser estudiante, departamento inscripcion o materia
        laColeccion = self.baseDatos[self.coleccion]#coleccion que se obtuvo al hacer la conexion con bd
        elId = ""   #variabel qeu luego se llena con un id
        item = self.__transformRefs(item)  #para hacer transformacion de ref de cada item
        if hasattr(item, "_id") and item._id != "":  #es decir cuando el atributo existe asi no tenga informacion
            elId = item._id   
            _id = ObjectId(elId) #convierte el id en un objeto
            laColeccion = self.baseDatos[self.coleccion]
            delattr(item, "_id")
            item = item.__dict__
            updateItem = {"$set": item}
            x = laColeccion.update_one({"_id": _id}, updateItem)
        else:   # si el objeto no existe   codigo para decir que se debe insertar uno nuevo
            _id = laColeccion.insert_one(item.__dict__)
            elId = _id.inserted_id.__str__()
        x = laColeccion.find_one({"_id": ObjectId(elId)})
        x["_id"] = x["_id"].__str__()
        return self.findById(elId)
    

    def delete(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        cuenta = laColeccion.delete_one({"_id": ObjectId(id)}).deleted_count
        return {"deleted_count": cuenta}

    def update(self, id, item: T):
        _id = ObjectId(id)
        laColeccion = self.baseDatos[self.coleccion]
        delattr(item, "_id")
        item = item.__dict__
        updateItem = {"$set": item}
        x = laColeccion.update_one({"_id": _id}, updateItem)
        return {"updated_count": x.matched_count}

    def findById(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"_id": ObjectId(id)})
        x = self.__getValuesDBRef(x)
        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def findAll(self):
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.find():
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __query(self, theQuery):             #convirtiendo el metodo a privado
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.find(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __queryAggregation(self, theQuery):      #convirtiendo el metodo a privado
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.aggregate(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __getValuesDBRef(self, x):
        keys = x.keys()
        for k in keys:
            if isinstance(x[k], DBRef):
                laColeccion = self.baseDatos[x[k].collection]
                valor = laColeccion.find_one({"_id": ObjectId(x[k].id)})
                valor["_id"] = valor["_id"].__str__()
                x[k] = valor
                x[k] = self.__getValuesDBRef(x[k])
            elif isinstance(x[k], list) and len(x[k]) > 0:
                x[k] = self.__getValuesDBRefFromList(x[k])
            elif isinstance(x[k], dict) :
                x[k] = self.__getValuesDBRef(x[k])
        return x

    def __getValuesDBRefFromList(self, theList):
        newList = []
        laColeccion = self.baseDatos[theList[0]._id.collection]
        for item in theList:
            value = laColeccion.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList

    def __transformObjectIds(self, x):
        for attribute in x.keys():
            if isinstance(x[attribute], ObjectId):
                x[attribute] = x[attribute].__str__()
            elif isinstance(x[attribute], list):
                x[attribute] = self.__formatList(x[attribute])
            elif isinstance(x[attribute], dict):
                x[attribute]=self.__transformObjectIds(x[attribute])
        return x

    def __formatList(self, x):
        newList = []
        for item in x:
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
        if len(newList) == 0:
            newList = x
        return newList

    def __transformRefs(self, item):
        theDict = item.__dict__
        keys = list(theDict.keys())
        for k in keys:
            if theDict[k].__str__().count("object") == 1:
                newObject = self.__ObjectToDBRef(getattr(item, k))
                setattr(item, k, newObject)
        return item

    def __ObjectToDBRef(self, item: T):
        nameCollection = item.__class__.__name__.lower()
        return DBRef(nameCollection, ObjectId(item._id)) 

