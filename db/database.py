import sqlite3
from tkinter import messagebox
from pathlib import Path

def conectarBBDD():
    try:
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()

        miCursor.execute('''
            CREATE TABLE USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(50) UNIQUE,
            CONTRASENA VARCHAR(50),
            GENERO VARCHAR(20),
            CIUDAD VARCHAR(30))
        ''')

        miConexion.close()
        messagebox.showinfo("Exito", "Base de Datos conectada con exito")

    except sqlite3.OperationalError:
        messagebox.showerror("Error!", "Base de Datos ya fue creada")
    
    except: 
        messagebox.showerror("Error!", "Error al conectar!")
    
    finally:
        miConexion.close()
    
def compruebaDB():

    fileObj = Path(r"./Usuarios")
    if fileObj.is_file():
        messagebox.showinfo("Base de Datos","Está conectada!")

    else:
        messagebox.showwarning("Advertencia", "No está conectada")

def estadoDB():

    fileObj = Path(r"./Usuarios")
    if fileObj.is_file():
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()

        miCursor.execute("SELECT count(ID) FROM USUARIOS")

        registros = miCursor.fetchall()

        for i in registros:
            if i[0] == 0:
                messagebox.showinfo("Estado", "Sin registros")
            
            else:
                messagebox.showinfo("Estado", "Registros: " + str(i[0]))
        
        miConexion.close()
    else:
        messagebox.showwarning("Advertencia", "Base de Datos no está conectada")


def contadorID():
    fileObj = Path(r"./Usuarios")

    if fileObj.exists() == True:
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()

        miCursor.execute("SELECT ID FROM USUARIOS ORDER BY ID")

        registros = miCursor.fetchall()
        miConexion.close()
        
        for i in registros:
            contador = i[0]

        return contador + 1
    
    else:
        return 1
    
# -------------------------------------------
# CRUD
# -------------------------------------------

