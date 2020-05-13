# ----------------------------------------------------------
# Imports
# ----------------------------------------------------------
from tkinter import *
from tkinter import messagebox
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
# ----------------------------------------------------------
idContador = IntVar()
opcionGenero = IntVar()
usuario = StringVar()
password = StringVar()
genero = StringVar()
ciudad = StringVar()

# ----------------------------------------------------------
# Metodos
# ----------------------------------------------------------
def insertarUsuario():
    

def verLicencia():
    messagebox.showinfo("Licencia", "Producto bajo licencia GNU")

def acercaDe():
    messagebox.showinfo("Acerca de...", "Sistema CRUD \nVersion: 1.0")


# ----------------------------------------------------------
# Menu
# ----------------------------------------------------------
barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

bbddMenu = Menu(barraMenu, tearoff = 0)
bbddMenu.add_command(label = "Conectar", command = db.conectarBBDD)
bbddMenu.add_command(label = "Comprobar Conexion", command = db.compruebaDB)
bbddMenu.add_separator()
bbddMenu.add_command(label = "Salir")

crudMenu = Menu(barraMenu, tearoff = 0)
crudMenu.add_command(label = "Insertar")
crudMenu.add_command(label = "Leer")
crudMenu.add_command(label = "Actualizar")
crudMenu.add_command(label = "Eliminar")

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
idCount = Label(frame, textvariable = idContador)

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

createButton = Button(frame, text = "Insertar").place(x = 30, y = 235)
readButton = Button(frame, text = "Leer").place(x = 90, y = 235)
updateButton = Button(frame, text = "Actualizar").place(x = 135, y = 235)
deleteButton = Button(frame, text = "Eliminar").place(x = 210, y = 235)

# ----------------------------------------------------------
# mainloop
# ----------------------------------------------------------
root.mainloop()
