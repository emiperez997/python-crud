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

