# ----------------------------------------------------------
# Imports
# ----------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
import db.database as db

# ----------------------------------------------------------
# root
# ----------------------------------------------------------
root = Tk()
root.title("Sistema CRUD")
root.resizable(0, 0)

# ----------------------------------------------------------
# Variables
# -----------------------------------------------------------

print()

idContador = StringVar()
idContador.set(str(db.contadorID()))
opcionGenero = IntVar()
usuario = StringVar()
password = StringVar()
genero = StringVar()
ciudad = StringVar()
actualizable = BooleanVar()
actualizable.set(False)

# ----------------------------------------------------------
# Metodos
# ----------------------------------------------------------

def insertarUsuario():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    gen = StringVar()

    if opcionGenero.get() == 1:
        gen.set("Masculino")
    else:
        gen.set("Femenino")


    if usuario.get() != '' and password.get() != '' and ciudad.get() != '':
        datos = (usuario.get(), password.get(), gen.get(), ciudad.get())

        try:
            miCursor.execute("INSERT INTO USUARIOS VALUES(NULL, ?, ?, ?, ?)", datos)

            miConexion.commit()

            messagebox.showinfo("Base de Datos", "Registro insertado con éxito")
        
        except:
            messagebox.showerror("Error!", "Oops! Algo salió mal")
        
        finally:
            miConexion.close()
            borrarCampos()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben ser rellenados")

def leerUsuario():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    buscar_usuario = simpledialog.askstring('Buscar Usuario', 'Ingrese el nombre de usuario: ')

    if buscar_usuario is not None:
        miCursor.execute("SELECT ID, USUARIO, CONTRASENA, GENERO, CIUDAD FROM USUARIOS WHERE USUARIO = '" + buscar_usuario + "'")

        usuario_encontrado = miCursor.fetchall()

        if usuario_encontrado != []:
            messagebox.showinfo("Usuario encontrado", usuario_encontrado)
            
            miConexion.close()
        
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")

def obtenerDatos():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    buscar_usuario = simpledialog.askstring('Actualizar Usuario', 'Ingrese el nombre de usuario: ')

    if buscar_usuario is not None:
        miCursor.execute("SELECT ID, USUARIO, CONTRASENA, GENERO, CIUDAD FROM USUARIOS WHERE USUARIO = '" + buscar_usuario + "'")

        usuario_encontrado = miCursor.fetchall()

        if usuario_encontrado != []:
            for usuario_db in usuario_encontrado:
                idContador.set(usuario_db[0])
                usuario.set(usuario_db[1])
                password.set(usuario_db[2])
                if usuario_db[3] == 'Masculino':
                    opcionGenero.set(1)
                elif usuario_db[3] == 'Femenino':
                    opcionGenero.set(2)
                ciudad.set(usuario_db[4])
            
            actualizable.set(True)
            
            miConexion.close()
        
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")


def actualizarUsuario():

    if actualizable.get() == False:
        obtenerDatos()
    else:
        
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()

        gen = StringVar()

        if opcionGenero.get() == 1:
            gen.set("Masculino")
        else:
            gen.set("Femenino")


        if usuario.get() != '' and password.get() != '' and ciudad.get() != '' and actualizable:
            datos = (usuario.get(), password.get(), gen.get(), ciudad.get())

            try:
                miCursor.execute("UPDATE USUARIOS SET USUARIO = ?, CONTRASENA = ?, GENERO = ?, CIUDAD = ? WHERE ID = " + idContador.get(), datos)

                miConexion.commit()

                messagebox.showinfo("Base de Datos", "Registro actualizado con éxito")
            
            except:
                messagebox.showerror("Error!", "Oops! Algo salió mal")
            
            finally:
                miConexion.close()
                borrarCampos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser rellenados")
    
def eliminarUsuario():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    buscar_usuario = simpledialog.askstring("Eliminar Usuario", "Ingrese el nombre de usuario a eliminar: ")

    if buscar_usuario is not None:
        miCursor.execute("DELETE FROM USUARIOS WHERE USUARIO = '" + buscar_usuario + "'")
        miConexion.commit()

        messagebox.showinfo("Eliminado", "Usuario eliminado con exito")
    
    miConexion.close()


def verLicencia():
    messagebox.showinfo("Licencia", "Producto bajo licencia GNU")

def acercaDe():
    messagebox.showinfo("Acerca de...", "Sistema CRUD \nVersion: 1.0")

def borrarCampos():
    idContador.set(str(db.contadorID()))
    usuario.set("") 
    password.set("") 
    opcionGenero.set(None) 
    ciudad.set("") 
    actualizable = False


# ----------------------------------------------------------
# Menu
# ----------------------------------------------------------
barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

bbddMenu = Menu(barraMenu, tearoff = 0)
bbddMenu.add_command(label = "Crear Conexion", command = db.conectarBBDD)
bbddMenu.add_command(label = "Comprobar Conexion", command = db.compruebaDB)
bbddMenu.add_command(label = "Comprobar Estado", command = db.estadoDB)
bbddMenu.add_separator()
bbddMenu.add_command(label = "Salir")

crudMenu = Menu(barraMenu, tearoff = 0)
crudMenu.add_command(label = "Insertar", command = insertarUsuario)
crudMenu.add_command(label = "Leer", command = leerUsuario)
crudMenu.add_command(label = "Actualizar", command = actualizarUsuario)
crudMenu.add_command(label = "Eliminar", command = eliminarUsuario)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "Ver Licencia", command = verLicencia)
ayudaMenu.add_command(label = "Acerca de...", command = acercaDe)

barraMenu.add_cascade(label = "Base de Datos", menu = bbddMenu)
barraMenu.add_cascade(label = "CRUD", menu = crudMenu)
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)



# ----------------------------------------------------------
# Formulario
# ----------------------------------------------------------
frame = Frame()
frame.config(width = "300", height = "280")
frame.pack()

titulo = Label(frame, text = "Bienvenido a nuestro sistema CRUD").place(x = 50, y = 10)

idLabel = Label(frame, text = "ID: ").place(x = 30, y = 40)
idCount = Label(frame, textvariable = idContador).place(x = 110, y = 40)

usuarioLabel = Label(frame, text = "Usuario: ").place(x = 30, y = 70)
usuarioEntry = Entry(frame, textvariable = usuario).place(x = 110, y = 70)

passwordLabel = Label(frame, text = "Contraseña: ").place(x = 30, y = 100)
passwordEntry = Entry(frame, textvariable = password)
passwordEntry.place(x = 110, y = 100)
passwordEntry.config(show = "*")

generoLabel = Label(frame, text = "Genero ").place(x = 30, y = 130)
Radiobutton(frame, text = "Masculino", variable = opcionGenero, value = 1).place(x = 110, y = 130)
Radiobutton(frame, text = "Femenino", variable = opcionGenero, value = 2).place(x = 110, y = 155)

ciudadLabel = Label(frame, text = "Ciudad: ").place(x = 30, y = 185)
ciudadEntry = Entry(frame, textvariable = ciudad).place(x = 110, y = 185)

createButton = Button(frame, text = "Insertar", command = insertarUsuario).place(x = 30, y = 235)
readButton = Button(frame, text = "Leer", command = leerUsuario).place(x = 90, y = 235)
updateButton = Button(frame, text = "Actualizar", command = actualizarUsuario).place(x = 135, y = 235)
deleteButton = Button(frame, text = "Eliminar", command = eliminarUsuario).place(x = 210, y = 235)

# ----------------------------------------------------------
# mainloop
# ----------------------------------------------------------
root.mainloop()
