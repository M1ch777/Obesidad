#Importamos la biblioteca para crear la interfase de la aplicacion
from tkinter import ttk
from tkinter import *
from typing import Collection #traigo todos los elementos de la biblioteca
import pymongo
import tkinter as tk
from tkinter import messagebox

from setuptools import Command

class Usuarios:
    '''
    Clase Usuarios.
    
    Atributos
    ----------
    nombre: str
        Nombre del Usuario
    apellido: str
        Apellido del Usuario
    sexo: str
        Sexo del Usuario
    edad: str
        Edad del Usuario
    usuario: str
        Registro de la cuenta del Usuario
    clave: str
        Clave con la que va acceder el Usuario a su cuenta
    
    Metodo
    ----------
    def __init__(self,nombre,apellido,sexo,edad,usuario,clave):
        Constructor de la clase
    def registroUsuario(self):
        En este apartado el usuario registrara sus datos mediante los parametros que le pediremos como nombre,apellido,sexo,edad,usuario y clave.
        sub Metodo
        ----------
        def getDatos ():
            Guarda los datos en la base de datos.
    def inicioSesion(self,usuario1,clave1):
        Permitira Iniciar sesión con el usuario y clave que registro el usuario.
    
    '''
    def __init__(self,nombre,apellido,sexo,edad,usuario,clave):
        '''
         Construye todos los atributos necesarios para el Usuario.

        Parametros
        ----------
        nombre: str
            Nombre del Usuario
        apellido: str
            Apellido del Usuario
        sexo: str
            Sexo del Usuario
        edad: str
            Edad del Usuario
        usuario: str
            Registro de la cuenta del Usuario
        clave: str
            Clave con la que va acceder el Usuario a su cuenta
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.edad=edad
        self.usuario=usuario
        self.clave=clave

    
    def registroUsuario(self):
        '''
        Metodo para Registrar a los Usuarios.
        Parametros
        ------------
        nombre: str
            Nombre del Usuario
        apellido: str
            Apellido del Usuario
        sexo: str
            Sexo del Usuario
        edad: str
            Edad del Usuario
        usuario: str
            Registro de la cuenta del Usuario
        clave: str
            Clave con la que va acceder el Usuario a su cuenta

        Retorna:
        ------------
        Una ventana con los parametros que le pediremos al Usuario final y esos datos se guardaran en la base de datos de MongoDB llamada BaseDataIMC.
        '''

        ventana.title('Registro de Usuarios')

        '''CREAMOS UN CONTENEDOR'''
        contenedor=LabelFrame(ventana, text='Registro de Usuario')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        '''CREAR ETIQUETAS CON SUS CAJAS DE TEXTO '''
        Label(contenedor,text='Nombres:').grid(row=1, column=0)
        nombre=Entry(contenedor)
        nombre.grid(row=1,column=1)

        Label(contenedor,text='Apellidos:').grid(row=2, column=0)
        apellido=Entry(contenedor)
        apellido.grid(row=2,column=1)

        Label(contenedor,text='Sexo:').grid(row=3, column=0)
        sexo=Entry(contenedor)
        sexo.grid(row=3,column=1)

        Label(contenedor,text='Edad:').grid(row=4, column=0)
        edad=Entry(contenedor)
        edad.grid(row=4,column=1)

        Label(contenedor,text='Usuario:').grid(row=5, column=0)
        usuario=Entry(contenedor)
        usuario.grid(row=5,column=1)

        Label(contenedor,text='Contraseña:').grid(row=6, column=0)
        clave=Entry(contenedor)
        clave.grid(row=6,column=1)

        def getDatos ():
            '''
            Metodo para guardar los datos.
            Parametros
            ------------
            nombre: str
                Nombre del Usuario
            apellido: str
                Apellido del Usuario
            sexo: str
                Sexo del Usuario
            edad: str
                Edad del Usuario
            usuario: str
                Registro de la cuenta del Usuario
            clave: str
                Clave con la que va acceder el Usuario a su cuenta
            Guardar:
            ------------
            Guarda los datos ingresado a la base de datos de MongoDB.
            '''
            '''Creación de un diccionario con los datos ingresados'''
            datosDic={'nombre': nombre.get(), 'apellido': apellido.get(), 'sexo': sexo.get(), 'edad': edad.get(), 'usuario': usuario.get(), 'clave': clave.get()}
            '''Agregamos nuetro diccionario a nuestra base de datos'''
            coleccion.insert_one(datosDic)
            self.mensaje['text']='Guardado satisfactoriamente'
            '''CREAMOS LA SALIDA DE MENSAJES DE ALERTA'''
            self.mensaje=Label(text='',fg='red')
            self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)
            
        '''Botón que registra los datos ingresados'''
        ttk.Button(contenedor, text='Guardar',command=getDatos).grid(row=9, column=0,sticky=W+E)

    
    def inicioSesion(self,usuario1,clave1):
        '''
        Metodo para Iniciar Sesión.
        Parametros
        ------------
        usuario: str
            Registro de la cuenta del Usuario
        clave: str
            Clave con la que va acceder el Usuario a su cuenta

        Retorna:
        ------------
        La nueva ventana donde pedira los ultimos datos para mostrar los resultados finales como la recetas, etc.
        '''

        ventana.title('Inicio de Sesión')

        '''CREAMOS UN CONTENEDOR'''
        contenedor=LabelFrame(ventana, text='Ingrese sus credenciales')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        '''CREAR ETIQUETAS CON SUS CAJAS DE TEXTO '''
        Label(contenedor,text='Usuario:').grid(row=1, column=0)
        usuario1=Entry(contenedor)
        usuario1.grid(row=1,column=1)

        Label(contenedor,text='Clave:').grid(row=2, column=0)
        clave1=Entry(contenedor)
        clave1.grid(row=2,column=1)

        """#CREAMOS LOS BOTONES
        ttk.Button(contenedor, text='Aceptar').grid(row=3, column=0,sticky=W+E)
        ttk.Button(contenedor, text='Cancelar').grid(row=3, column=1,sticky=W+E)"""
        
        '''CREAMOS LA SALIDA DE MENSAJES DE ALERTA'''
        self.mensaje=Label(text='',fg='red')
        self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)
        ttk.Button(contenedor, text='Aceptar',command = lambda: validar(usuario1.get(), clave1.get()) ).grid(row=3, column=0,sticky=W+E)
"""        tk.Button(ventana, text= "Confirmar", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat", command = lambda: validar(usuario1.get()) ) """


    
"""
        ttk.Button(contenedor, text='Guardar').grid(row=9, column=0,sticky=W+E)
        ttk.Button(contenedor, text='Eliminar').grid(row=9, column=1,sticky=W+E)
        ttk.Button(contenedor, text='Editar').grid(row=10, column=0,sticky=W+E)
        ttk.Button(contenedor, text='Salir').grid(row=10, column=1,sticky=W+E)   """



class Control:
    '''
    Clase Control. 

    Atributos
    --------------
    peso: float
        Peso del Usuario en [kg].
    estatura: float
        Estatura del Usuario en [m].
    edad: float
        Edad del Usuario.
    Metodos
    --------------
    def __init__(self, peso, estatura, edad):
        Construye todos los atributos necesarios para el objeto Control.
    def datosIMC(self):
        Usamos los datos obtenidos utilizamos la formula IMC para mostrar el peso ideal segun los datos obtenidos.
        sub Metodo
        -----------
        def calculoIMC():
            Formula para calcular el peso ideal con los datos obtenidos del usuario.
        def getDatos1 ():
            Guarda el peso,edad y estatura en nuestra base de datos.
    def historial(self):
        Muestra un historial de los todos los datos que se han ingresado.
    '''
    def __init__(self, peso, estatura, edad):
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
    
    def datosIMC(self):
        ventana.title('Control de Indice de Masa Corporal')

        #CREAMOS UN CONTENEDOR
        contenedor=LabelFrame(ventana, text='Datos Requeridos')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        #CREAR ETIQUETAS CON SUS CAJAS DE TEXTO 
        Label(contenedor,text='Peso [Kg]:').grid(row=1, column=0)
        peso=Entry(contenedor)
        peso.grid(row=1,column=1)

        Label(contenedor,text='Estatura [m]:').grid(row=2, column=0)
        estatura=Entry(contenedor)
        estatura.grid(row=2,column=1)

        Label(contenedor,text='Edad:').grid(row=3, column=0)
        edad=Entry(contenedor)
        edad.grid(row=3,column=1)

        Label(contenedor,text='Fecha:').grid(row=4, column=0)
        fecha=Entry(contenedor)
        fecha.grid(row=4,column=1)

        def calculoIMC():

            x=float(estatura.get())
            y=float(peso.get())
            imc=float(y/(x**2))   

            if imc > 24.9:
                mensaje="Usted esta' con sobrepeso"
            elif imc<18.5:
                mensaje="Usted esta' por debajo su peso ideal"
            else:
                mensaje="Se encuentra con un peso ideal."
            
            messagebox.showinfo('Informacion',mensaje)   


        def getDatos1 ():
            '''Creación de un diccionario con los datos ingresados'''
            datosDic1={'peso': peso.get(), 'estatura': estatura.get(), 'edad': edad.get()}
            '''Agregamos nuetro diccionario a nuestra base de datos'''
            coleccion1.insert_one(datosDic1)
            self.mensaje['text']='Guardado satisfactoriamente'
            #CREAMOS LA SALIDA DE MENSAJES DE ALERTA
            self.mensaje=Label(text='',fg='red')
            self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)
            calculoIMC()
        
        '''Botón que registra los datos ingresados'''
        ttk.Button(contenedor, text='Guardar',command=getDatos1).grid(row=9, column=0,sticky=W+E)

        '''CREAMOS LA SALIDA DE MENSAJES DE ALERTA'''
        self.mensaje=Label(text='',fg='red')
        self.mensaje.grid(row=7,column=0,columnspan=2,sticky=W+E)

    def historial(self):
        '''
        Metodo para mostar un historial de los datos guardados en la base de datos.
        Retorna:
        ------------
        Retorna la lista de datos mostrada a cada usuario.
        
        CREAMOS UNA VISTA DE DATOS'''
        columnas = ('#1', '#2', '#3', '#4', '#5', '#6')
        self.vista=ttk.Treeview(height=10,columns=columnas)
        self.vista.grid(row=8,column=0, columnspan=2)
        self.vista.heading('#0',text='Fecha',anchor=CENTER)
        self.vista.heading('#1',text='Peso',anchor=CENTER)
        self.vista.heading('#2',text='Estatura',anchor=CENTER)
        self.vista.heading('#3',text='Edad',anchor=CENTER)
        self.vista.heading('#4',text='IMC',anchor=CENTER)
        self.vista.heading('#5',text='Observacion',anchor=CENTER)


def queryUsuarioContra():
    '''
    Metodo queryUsuarioContra().
    Retorna:
    ------------
    Retorna el usuario y contraseña y verifica que este en la lista.
    '''
    coleccionFinal=coleccion.find()
    coleccionUsuarios=[]
    for i in coleccionFinal:
        coleccionUsuarios.append(i['usuario'])
        coleccionUsuarios.append(i['clave'])
    return coleccionUsuarios

def validar(usuario2, clave2):
    '''
    Metodo validar el usuario y la contraseña.
    Parametros
    ------------
    usuario2: str
        Usuario del usuario.
    clave2: str
        Clave del usuario.

    Retorna:
    ------------
    Verifica si el usuario y la contraseña se encuentran en la base de datos y que sean validas.
    '''
    if usuario2 and clave2 in queryUsuarioContra(): # Verificamos que el usuario y la clave pertenescan a la queryUsuarioContra().
        Control("","","").datosIMC()
        
    else:
        messagebox.showwarning("Error", "Usuario o contrasena in orrecto") # Caso contrario nos muestra el mensaje de error.


if __name__== '__main__':
    '''Creación de la base de datos BaseDataIMC y la colección Usuarios y Controles en MongoDB'''
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    MONGO_BASED = "BaseDataIMC"
    COLECCION = "Usuarios"
    baseDatos = myClient[MONGO_BASED]
    coleccion = baseDatos [COLECCION]

    COLECCION1 = "Controles"
    coleccion1 = baseDatos[COLECCION1]

    ventana= Tk()
    #aplicacion=Usuarios(ventana)
    #aplicacion=Inicio_Sesion(ventana)
    aplicacion=Usuarios("","","", "", "", "")
    aplicacion.inicioSesion("","")
    ventana.mainloop()
    
