from tkinter import *
from IMC_Clases import *
import pymongo

if __name__== '__main__':
    '''Creación de la base de datos BaseDataIMC y la colección Usuarios en MongoDB'''
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    MONGO_BASED = "BaseDataIMC"
    COLECCION = "Usuarios"
    baseDatos=myClient[MONGO_BASED]
    coleccion = baseDatos [COLECCION]

    ventana = Tk()
    #aplicacion=Usuarios(ventana)
    #aplicacion=Inicio_Sesion(ventana)
    aplicacion=Usuarios(ventana)
    aplicacion=Control(ventana)
    ventana.mainloop()