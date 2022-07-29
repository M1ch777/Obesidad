"""Importamos la biblioteca para crear la interfase de la aplicacion"""
import sys
from tkinter import dialog, ttk
from tkinter import * #traigo todos los elementos de la biblioteca
import tkinter as tk
from tkinter import messagebox
from bson.objectid import ObjectId
from datetime import date
from PIL import ImageTk, Image

#HAGO LA CONEXION CON MONGODB
from pymongo import MongoClient
MongoUrl='mongodb://localhost'
cliente=MongoClient(MongoUrl)
Bd=cliente['IMC']

class Usuarios:
    '''
    Clase Usuarios.
    
    Atributos
    ----------
    nombre: str
        ventana destinada a interfaces
    apellido: str
        Apellido del Usuario
    correo: str
        correo del Usuario
    usuario: str
        usuario de la persona
    clave: str
        Clave con la que va acceder el Usuario a su cuenta
    
    Metodo
    ----------
    def __init__(self, nombre,apellido,correo,usuario,clave,sexo):
        Constructor de la clase
        
    def registroUsuario(self):
        En este apartado el usuario registrara sus datos mediante los parametros que le pediremos
        sub Metodos
        ----------
        def guardar():
            guarda los datos en la base de datos

        def eliminar():
            elimina datis de la base de datos

        def editar():
            edita datos dentro de la base de datos

        def actualizar():
            actualiza la base de datos con los que habian sido editados
        
        def validar()
            exige al usuario llenar todos los campos para el registro
        
        def limpiar():
            limpia las cajas de texto.

    def obtenerVista(self):
        permite visualizar los usuarios registrados y algunos
        detalles mas.

    
    '''

    def __init__(self,nombre,apellido,correo,usuario,clave,sexo):
        '''
         Construye todos los atributos necesarios para el Usuario.

        Parametros
        ----------
        nombre: str
            Nombre del Usuario
        apellido: str
            Apellido del Usuario
        correo: str
            correo del Usuario
        usuario: str
            usuario a registrar
        clave: str
            Clave con la que va acceder el Usuario a su cuenta
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.usuario=usuario
        self.clave=clave
        self.sexo=sexo

    def registroUsuario(self, ventana):
        
        """Permite que el usuario se registre
        ingresando una serie de datos.

        Parametros
        ----------
        ventana: str
            permite crear las interfaces
        """
        self.window=ventana
        self.window.title('Registro de Usuarios')
        self.window.geometry("1600x600")
        
        """ESTABLECEMOS LA COLECCION QUE PÉRTENECE LA CLASE"""
        self.coleccion=Bd['Usuarios']

        """CREAMOS DOS CONTENEDORES"""
        contenedor=LabelFrame(self.window, text='Registro de Usuario')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        contenedorLv=LabelFrame(self.window, text='')
        contenedorLv.grid(row=15, column=0, columnspan=2,pady=5)
        

        """CREAR ETIQUETAS CON SUS CAJAS DE TEXTO"""
        Label(contenedor,text='Nombres:').grid(row=1, column=0)
        self.nombre=Entry(contenedor,validate="key")
        self.nombre.grid(row=1,column=1)
        
        Label(contenedor,text='Apellidos:').grid(row=2, column=0)
        self.apellido=Entry(contenedor)
        self.apellido.grid(row=2,column=1)

        Label(contenedor,text='Correo:').grid(row=3, column=0)
        self.correo=Entry(contenedor)
        self.correo.grid(row=3,column=1)

        Label(contenedor,text='Usuario:').grid(row=4, column=0)
        self.usuario=Entry(contenedor)
        self.usuario.grid(row=4,column=1)

        Label(contenedor,text='Contraseña:').grid(row=5, column=0)
        self.clave=Entry(contenedor)
        self.clave.grid(row=5,column=1)

        Label (contenedor, text="Sexo",bg = "gold").grid(row=6, column=0)
        self.sexo = Entry (contenedor)
        self.sexo=StringVar(contenedor)
        opcionesSexo=["Masculino","Femenino"]
        opcionesSexo=OptionMenu(contenedor,self.sexo,*opcionesSexo)
        opcionesSexo.grid(row=6, column=1, columnspan=1,pady=5)


        """CREAMOS UNA VISTA DE DATOS"""
        columnas = ('#1', '#2', '#3', '#4', '#5')
        self.vista=ttk.Treeview(contenedorLv,height=14,columns=columnas)
        self.vista.grid(row=13,column=0, columnspan=2)
        self.vista.heading('#0',text='Id',anchor=CENTER)
        self.vista.heading('#1',text='Nombres',anchor=CENTER)
        self.vista.heading('#2',text='Apellidos',anchor=CENTER)
        self.vista.heading('#3',text='Correo',anchor=CENTER)
        self.vista.heading('#4',text='Sexo',anchor=CENTER)

        """LLENAMOS DE DATOS LA VISTA"""
        self.ObtenerVista()
        
        """SEB-METODO PARA GUARDAR UN REGISTRO"""
        def Guardar():
            """REALIZAMOS EL GUARDADO DEL REGISTRO SI ES QUE NO HAY ERRORES"""
            try:
                if validar():
                    """PASAMOS EL DATO QUE SE ENCUENTRA EN LAS CAJAS DE TEXTO COMO PARAMETRO DE CADA ELEMENTO DE LA COLECCION"""
                    self.coleccion.insert_one({"nombres":self.nombre.get(),"apellidos":self.apellido.get(),
                    "correo":self.correo.get(),"usuario":self.usuario.get(),"clave":self.clave.get(),"sexo":self.sexo.get()})
                    messagebox.showinfo('Guardando','Se guardó correctamente el registro actual.')
                    self.ObtenerVista()
                    limpiarCajas()
                    
                else:
                    messagebox.showwarning("Error de validación","Ingrese información requerida, hay campos sin llenar.")
            except Exception:
                e=sys.exc_info()[1]
                messagebox.showerror('Error',e.args[0])

        def Eliminar():
            """ SUB-METODO PARA ELIMINAR UN REGISTRO"""
            """REALIZAMOS LA ELIMINACION DEL REGISTRO SI ES QUE NO HAY ERRORES"""
            try:
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                self.vista.item(self.vista.selection())['text'][0]
            except IndexError as e:
                messagebox.showerror("Error","Seleccione un registro para eliminar.")
                return
            if messagebox.askyesno("Confirmación","¿Esta seguro de eliminar el registro seleccionado?")==YES:
                """SE ELIMINA EL REGISTRO SELECCIONADO"""
                id=str(self.vista.item(self.vista.selection())['text'])
                idBuscar={"_id":ObjectId(id)}
                self.coleccion.delete_one(idBuscar)
                messagebox.showinfo('Eliminando','Se eliminó correctamente el registro actual.')
                self.ObtenerVista()
            else:
                messagebox.showinfo("Registros no afectados","No se eliminó ningún registro por que no se confirmó.")

        def Actualizar():
            """SUB-METODO PARA ACTUALIZAR UN REGISTRO"""
            if validar():
                #CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)
                id=str(self.vista.item(self.vista.selection())['text'])
                idBuscar={"_id":ObjectId(id)}
                nuevosValores= {"$set": {"nombres":self.nombre.get(),"apellidos":self.apellido.get(),
                "correo":self.correo.get(),"usuario":self.usuario.get(),"clave":self.clave.get(),"sexo":self.sexo.get()}}
                #PASAMOS EL DATO QUE SE ENCUENTRA EN LAS CAJAS DE TEXTO COMO PARAMETRO DE CADA ELEMENTO DE LA COLECCION
                self.coleccion.update_one(idBuscar,nuevosValores)
                messagebox.showinfo('Actualizando','Se actualizo correctamente el registro actual.')
                self.ObtenerVista()
                limpiarCajas()
            else:
                messagebox.showwarning("Error de validación","Ingrese información requerida, hay campos sin llenar.")


        """METODO PARA ACTUZALIZAR UN REGISTRO"""
        def Editar():
            """VERIFICAMOS QUE SE HAYA SELECCIONADO EL REGISTRO A EDITAR"""
            try:
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                self.vista.item(self.vista.selection())['text'][0]
            except IndexError as e:
                messagebox.showerror("Error","Seleccione un registro para editar.")
                return
            
            """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
            id=str(self.vista.item(self.vista.selection())['text'])
            idBuscar={"_id":ObjectId(id)}
            resultado=self.coleccion.find_one(idBuscar)

            """SE LIMPIAN LOS CUADRO DE TEXTO PRIMERO"""
            limpiarCajas()

            self.nombre.insert(0,str(resultado['nombres']))
            self.apellido.insert(0,str(resultado['apellidos']))
            self.correo.insert(0,str(resultado['correo']))
            self.usuario.insert(0,str(resultado['usuario']))
            self.clave.insert(0,str(resultado['clave']))
            self.sexo.insert(0,str(resultado['sexo']))

            
        def validar():
            """VALIDACION DE LOS DATOS"""
            return len(self.nombre.get())!=0 and len(self.apellido.get())!=0 and len(self.correo.get())!=0 and len(self.usuario.get())!=0 and len(self.clave.get())!=0 and len(self.sexo.get())!=0

        def limpiarCajas():
            """Limpia las cajas de texto"""
            self.nombre.delete(0,END)
            self.apellido.delete(0,END)
            self.correo.delete(0,END)
            self.usuario.delete(0,END)
            self.clave.delete(0,END)


        def Salir():
            """Elimina la interfaz creada"""
            ventana.destroy()
                             
        
        """CREAMOS LOS BOTONES QUE VAMOS A DEJAR ACTIVOS EN LA EDICION"""
        ttk.Button(contenedor, text='Guardar',command=Guardar).grid(row=7, column=0)
        ttk.Button(contenedor, text='Eliminar',command=Eliminar).grid(row=7, column=1)
        ttk.Button(contenedor, text='Actualizar',command=Actualizar).grid(row=8, column=0)
        ttk.Button(contenedor, text='Salir',command=Salir).grid(row=8, column=1,sticky=W+E)  
        ttk.Button(contenedor, text='Editar',command=Editar).grid(row=9, column=0,sticky=W+E)  

    
    def ObtenerVista(self):
        """METODO PARA CONSULTAR LA COLECCION COMPLETA"""
        registros=self.vista.get_children()
        for elemento in registros:
            self.vista.delete(elemento)
        #Consultando los datos
        resultados=self.coleccion.find({})
        #llenando los datos
        for Fila in resultados:
           self.vista.insert('', 0, text= Fila["_id"],
            values = (Fila["nombres"],Fila["apellidos"],Fila["correo"],Fila["sexo"]))
           
  

       
class Inicio_Sesion:
    '''
    Clase Inicio_Sesion.
    
    Atributos
    ----------
    usuario: str
        usuario para acceder a la cuenta
    clave: str
        Clave con la que va acceder el Usuario a su cuenta
    
    Metodo
    ----------
    def __init__(self, usuario, clave):
        Constructor de la clase
        
        En este apartado el usuario validara' sus datos para comprobar
        si se enuentra o no registrado
        ----------
        def validarAcceso()
            valida que los datos sean correctos
        
        def Salir():
            sale de la interfaz.
        '''
    def __init__(self, usuario, clave):
        '''
         Construye todos los atributos necesarios para el Usuario.

        Parametros
        ----------
        usuario: str
            Registro del usuario de la cuenta
        clave: str
            Clave con la que va acceder el Usuario a su cuenta
        '''
        self.usuario=usuario
        self.clave=clave
    
    def inicioSesion(self, ventana):
        """Permite que el usuario ingrese sus credenciales
        para verificar si ya se registro'.

        Parametros
        ----------
        ventana: str
            permite crear las interfaces

        """
        """creacion de la interfaz 'Inicio de Sesion' """
        self.window=ventana
        self.window.title('Inicio de Sesión')
        self.window.geometry("200x100+550+350")

        """ESTABLECEMOS LA COLECCION QUE PÉRTENECE LA CLASE"""
        self.coleccion=Bd['Usuarios']

        """CREAMOS UN CONTENEDOR"""
        contenedor=LabelFrame(self.window, text='Ingrese sus credenciales')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        """CREAR ETIQUETAS CON SUS CAJAS DE TEXTO """
        Label(contenedor,text='Usuario:').grid(row=1, column=0)
        self.usuario=Entry(contenedor)
        self.usuario.grid(row=1,column=1)

        Label(contenedor,text='Clave:').grid(row=2, column=0)
        self.clave=Entry(contenedor)
        self.clave.grid(row=2,column=1)

        def ValidarAcceso():
            """EVALUAMOS SI TIENE ACCESO O NO"""
            idBuscar={"usuario":str(self.usuario.get()),"clave":str(self.clave.get())}
            resultados=self.coleccion.find_one(idBuscar)
            if resultados==None:
                messagebox.showwarning("Acceso Denegado","Usuario o Contraseña no existe.")
            else:
                ControlVentana = Toplevel()
                aplicacion=Control("","","")
                aplicacion.CalculosIMC(ControlVentana)
                ControlVentana.transient(master=self.window)
                ControlVentana.grab_set()
                self.window.wait_window(ControlVentana)
            Salir()
            

        def Salir():
            """CREAMOS EL SUB-METODO PARA SALIR DE LA VENTANA"""
            ventana.destroy()

        """CREAMOS LOS BOTONES"""
        ttk.Button(contenedor, text='Aceptar',command=ValidarAcceso).grid(row=3, column=0,sticky=W+E)
        ttk.Button(contenedor, text='Cancelar',command=Salir).grid(row=3, column=1,sticky=W+E)
        


class Control:
    '''
    Clase Usuarios.
    
    Atributos
    ----------
    peso : str
        peso del usuario
    altura: str
        altura del Usuario
    edad: str
        edad del Usuario
    
    Metodo
    ----------
    def __init__(self, self, peso, estatura, edad):
        Constructor de la clase
        
    def calculosIMC(self):
        En este apartado se realizan los calculos del IMC para determinar en que estado de
        peso se encuentr

        Sub-Metodos 
        ----------
        def guardar():
            guarda los datos en la base de datos

        def eliminar():
            elimina datis de la base de datos

        def editar():
            edita datos dentro de la base de datos

        def actualizar():
            actualiza la base de datos con los que habian sido editados
        
        def validar()
            exige al usuario llenar todos los campos para el registro
        
        def limpiar():
            limpia las cajas de texto.

    def calculoIMC():
        determina la etapa exacta de la masa corporal del usuario, partiendo por su IMC

    def obtenerVista(self):
        permite visualizar los datos acerca de los controles registrados y algunos
        detalles mas.
    '''

    def __init__(self, peso, estatura, edad):
        '''
         Construye todos los atributos necesarios para el Usuario.

        Parametros
        ----------
        peso: float
            peso del usuario
        estatura: float
            estatura del usuario
        edad: int
            edad del usuario
        '''

        self.peso=peso
        self.estatura=estatura
        self.edad=edad
    
    def CalculosIMC(self, ventana):
        """Permite que el usuario ingrese sus datos como peso, altura, edad
        para gnerar el imc.

        Parametros
        ----------
        ventana: str
            permite crear las interfaces

        """
        self.window=ventana
        self.window.title('Control de Indice de Masa Corporal')
        self.window.geometry("1200x650")

        """ESTABLECEMOS LA COLECCION QUE PÉRTENECE LA CLASE"""
        self.coleccion=Bd['Controles']

        """CREAMOS UN CONTENEDOR PARA LAS CAJAS DE TEXTO Y BOTONES"""
        contenedor=LabelFrame(self.window, text='Datos Requeridos')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        """CREAR ETIQUETAS CON SUS CAJAS DE TEXTO """
        Label(contenedor,text='Peso [kg]:').grid(row=1, column=0)
        self.peso=Entry(contenedor)
        self.peso.grid(row=1,column=1)

        Label(contenedor,text='Estatura [m]:').grid(row=2, column=0)
        self.estatura=Entry(contenedor)
        self.estatura.grid(row=2,column=1)

        Label(contenedor,text='Edad:').grid(row=3, column=0)
        self.edad=Entry(contenedor)
        self.edad.grid(row=3,column=1)

        Label(contenedor,text='Fecha:').grid(row=4, column=0)
        self.fecha=Entry(contenedor)
        self.fecha.grid(row=4, column=1)
        self.fecha.insert(0,str(date.today()))


        Label(contenedor,text='IMC:').grid(row=5, column=0)
        self.imc=Entry(contenedor)
        self.imc.grid(row=5, column=1)
        
        Label(contenedor,text='Estado:').grid(row=6, column=0)
        self.observaciones=Entry(contenedor)
        self.observaciones.grid(row=6, column=1)

        """CREAMOS EL CONTENEDOR PARA EL LISTVIEW"""
        contenedorLv=LabelFrame(self.window, text='')
        contenedorLv.grid(row=14, column=0, columnspan=2,pady=5)

        """CREAMOS UNA VISTA DE DATOS"""
        columnas = ('#1', '#2', '#3', '#4', '#5','#6','#7')
        self.vista=ttk.Treeview(contenedorLv,height=17,columns=columnas)
        self.vista.grid(row=9,column=0, columnspan=10,padx=5)
        self.vista.column('#0',width=200)
        self.vista.column('#1',width=100)
        self.vista.column('#2',width=100)
        self.vista.column('#3',width=100)
        self.vista.column('#4',width=100)
        self.vista.column('#5',width=100)
        self.vista.column('#6',width=280)
        self.vista.heading('#0',text='Id',anchor=CENTER)
        self.vista.heading('#1',text='Fecha',anchor=CENTER)
        self.vista.heading('#2',text='Peso [Kg]',anchor=CENTER)
        self.vista.heading('#3',text='Estatura [m]',anchor=CENTER)
        self.vista.heading('#4',text='Edad',anchor=CENTER)
        self.vista.heading('#5',text='IMC',anchor=CENTER)
        self.vista.heading('#6',text='Estado',anchor=CENTER)

    
        """LLENAMOS DE DATOS LA VISTA"""
        self.ObtenerVista()
       


        """ METODO PARA GUARDAR UN REGISTRO"""
        def Guardar():
            """REALIZAMOS EL GUARDADO DEL REGISTRO SI ES QUE NO HAY ERRORES"""
            try:
                if validar():
                    """PASAMOS EL DATO QUE SE ENCUENTRA EN LAS CAJAS DE TEXTO COMO PARAMETRO DE CADA ELEMENTO DE LA COLECCION"""
                    self.coleccion.insert_one({"fecha":self.fecha.get(),"peso":self.peso.get(),"estatura":self.estatura.get(),
                    "edad":self.edad.get(), "imc": self.imc.get(),"estado": self.observaciones.get()})
                    messagebox.showinfo('Guardando','Se guardó correctamente el registro actual.')
                    self.ObtenerVista()
                    limpiarCajas()
                    """SE VUELVE A ASIGNAR LA FECHA ACTUAL"""
                    self.fecha.insert(0,date.today())
                    
                else:
                    messagebox.showwarning("Error de validación","CAMPOS SIN LLENAR.")
            except Exception:
                e=sys.exc_info()[1]
                messagebox.showerror('Error',e.args[0])

        """SUB-METODO PARA ELIMINAR UN REGISTRO"""
        def Eliminar():
            """REALIZAMOS LA ELIMINACION DEL REGISTRO SI ES QUE NO HAY ERRORES"""
            try:
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                self.vista.item(self.vista.selection())['text'][0]
            except IndexError as e:
                messagebox.showerror("Error","Seleccione un registro para eliminar.")
                return
            if messagebox.askyesno("Confirmación","¿Esta seguro de eliminar el registro seleccionado?")==YES:
                #SE ELIMINA EL REGISTRO SELECCIONADO
                id=str(self.vista.item(self.vista.selection())['text'])
                idBuscar={"_id":ObjectId(id)}
                self.coleccion.delete_one(idBuscar)
                messagebox.showinfo('Eliminando','Se eliminó correctamente el registro actual.')
                self.ObtenerVista()
            else:
                messagebox.showinfo("Registros no afectados","No se eliminó ningún registro por que no se confirmó.")

        """SUBMETODO PARA ACTUZALIZAR UN REGISTRO"""
        def Actualizar():
            """REALIZAMOS LA ACTUALIZACION DEL REGISTRO SI ES QUE NO HAY ERRORES"""
            try:
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                self.vista.item(self.vista.selection())['text'][0]
            except IndexError as e:
                messagebox.showerror("Error","Seleccione un registro para editar.")
                return
          
            if validar():
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                id=str(self.vista.item(self.vista.selection())['text'])
                idBuscar={"_id":ObjectId(id)}
                nuevosValores= {"$set": {"fecha":self.fecha.get(),"peso":self.peso.get(),"estatura":self.estatura.get(),
                "edad":self.edad.get(),"imc":self.imc.get(),"estado":self.observaciones.get()}}
                
                """PASAMOS EL DATO QUE SE ENCUENTRA EN LAS CAJAS DE TEXTO COMO PARAMETRO DE CADA ELEMENTO DE LA COLECCION"""
                self.coleccion.update_one(idBuscar,nuevosValores)
                messagebox.showinfo('Actualizando','Se actualizo correctamente el registro actual.')
                self.ObtenerVista()
                limpiarCajas()
                
            else:
                messagebox.showwarning("Error de validación","CASILLAS VACIAS")

            

        """VALIDACION DE LOS DATOS"""
        def validar():
            return len(self.fecha.get())!=0 and len(self.peso.get())!=0 and len(self.estatura.get())!=0 and len(self.edad.get())!=0 

        def limpiarCajas():
            """Limpia las cajas de texto"""
            self.fecha.delete(0,END)
            self.peso.delete(0,END)
            self.estatura.delete(0,END)
            self.edad.delete(0,END)    
            self.imc.delete(0,END)   
            self.observaciones.delete(0,END)

        def Salir():
            """Destruye la interfaz creada"""
            ventana.destroy()

        def Editar():
            """VERIFICAMOS QUE SE HAYA SELECCIONADO EL REGISTRO A EDITAR"""
            try:
                """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
                self.vista.item(self.vista.selection())['text'][0]
            except IndexError as e:
                messagebox.showerror("Error","Seleccione un registro para editar.")
                return
            
            """CAPTURAMOS EL ID DEL REGISTRO SELECCIONADO EN LA VISTA(LISTVIEW)"""
            id=str(self.vista.item(self.vista.selection())['text'])
            idBuscar={"_id":ObjectId(id)}
            resultado=self.coleccion.find_one(idBuscar)

            """SE LIMPIAN LOS CUADRO DE TEXTO PRIMERO"""
            limpiarCajas()

            self.fecha.insert(0,str(resultado['fecha']))
            self.peso.insert(0,str(resultado['peso']))
            self.estatura.insert(0,str(resultado['estatura']))
            self.edad.insert(0,str(resultado['edad']))
            self.imc.insert(0,str(resultado['imc']))
            

        def calculoIMC():
            """SUB-METODO QUE CALCULA EL IMC Y EN QUE ESTADO DE PESO SE ENCUENTRA"""
            if validar():
                x=float(self.estatura.get())
                y=float(self.peso.get())
                imc1=float(y/(x**2))
                
                imcR=round(imc1,2)
                self.imc.delete(0,END)
                self.imc.insert(0,str(round(imcR,2)))
                self.observaciones.delete(0,END)
                imcR=float(self.imc.get())
                
                """ESTABLECEMOS EN QUE RANGO DE LA TABLA IMC ESTA EL USUARIO"""
                if float(imcR)<float(18.5):
                    self.observaciones.insert(0,"Peso Bajo")
                elif 24.9 > float(imcR) > 18.5:
                    self.observaciones.insert(0,"Peso Normal")
                elif float(imcR)>24.9:
                    self.observaciones.insert(0,"Sobrepeso")
                elif 29.9 > float(imcR) < 25:
                    self.observaciones.insert(0,"Preobesidad")
                elif float(imcR)>29.9:
                    self.observaciones.insert(0,"Obesidad")
                else:
                    messagebox.showwarning("Error", "CASILLAS VACIAS." )
    
            
        """CREAMOS LOS BOTONES QUE VAMOS A DEJAR ACTIVOS EN LA EDICION"""
        ttk.Button(contenedor, text='Guardar',command=Guardar).grid(row=10, column=0,sticky=W+E)
        ttk.Button(contenedor, text='Eliminar',command=Eliminar).grid(row=10, column=1,sticky=W+E)
        ttk.Button(contenedor, text='Editar',command=Editar).grid(row=11, column=0,sticky=W+E)
        ttk.Button(contenedor, text='IMC',command=calculoIMC).grid(row=11, column=1,sticky=W+E)
        ttk.Button(contenedor, text='Actualizar',command=Actualizar).grid(row=12, column=0,sticky=W+E) 
        ttk.Button(contenedor, text='Salir',command=Salir).grid(row=12, column=1,sticky=W+E)  


        
    """METODO PARA CONSULTAR LA COLECCION COMPLETA"""
    def ObtenerVista(self):
        #Limpiando la vista
        registros=self.vista.get_children()
        for elemento in registros:
            self.vista.delete(elemento)
        #Consultando los datos
        resultados=self.coleccion.find({})
        #llenando los datos
        for Fila in resultados:
           self.vista.insert('', 0, text= Fila["_id"],
            values = (Fila["fecha"],Fila["peso"],Fila["estatura"],Fila["edad"],Fila["imc"],Fila['estado']))

        
class menuPrincipal:
    '''
    Clase Usuarios.
    
    Atributos
    ----------
    ventana:str
        crea la interfaz correspondiente
    
    Metodo
    ----------
    def __init__(self, ventana):
        Constructor de la clase
        
    def salir(self):
        sale por completo del programa/cierra interfaces.

    def Registrarse():
        permite abrir las interfaces de la clase Usuario

    def obtenerVista(self):
        permite visualizar las interfaces de la clase Control

    
    '''
    def __init__(self,ventana):
        """
        Metodo constructor
        ---------------
        """
        self.window=ventana
        self.window.title('Menu Principal Control de Indice de Masa Corporal')
        self.window.geometry("600x200+400+300")
              
        """CREAMOS UN CONTENEDOR"""
        contenedor=LabelFrame(self.window, text='Menu Principal')
        contenedor.grid(row=0, column=0, columnspan=2,pady=5)

        #CIERRA LA VENTANA ACTUAL
        def Salir():
            """Destruye todas las interfaces"""
            ventana.destroy()

        def Registrarse():
            """Metodo que permite abrir las interfaces correspondiente al
            registro de los Usuarios"""
            RegVentana = Toplevel()
            aplicacion=Usuarios("","","","","","")
            aplicacion.registroUsuario(RegVentana)
            RegVentana.transient(master=self.window)
            RegVentana.grab_set()
            self.window.wait_window(RegVentana)
        
        def Control():
            """metodo que abre la interfaz correspondiente a control"""
            SesionVentana = Toplevel()
            aplicacion=Inicio_Sesion("","")
            aplicacion.inicioSesion(SesionVentana)
            SesionVentana.transient(master=self.window)
            SesionVentana.grab_set()
            self.window.wait_window(SesionVentana)

        """CREAMOS LOS BOTONES"""
        ttk.Button(contenedor, text='CONTROL DE IMC',command=Control).grid(row=4, column=0,sticky=W+E)
        ttk.Button(contenedor, text='REGISTRARSE',command=Registrarse).grid(row=4, column=1,sticky=W+E)
        ttk.Button(contenedor, text='SALIR', command=Salir).grid(row=4, column=2,sticky=W+E)

        

        
            
            