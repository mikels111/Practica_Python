#import mysql.connector

"""

 ######## CON MYSQL NO HE PODIDO ########

"""
import sqlite3
import datetime
'''database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Cebanc1920",
    database = "proyecto_python",
    port = 3306
)'''
#cursor = database.cursor(buffered=True)

# Conexión
conexion = sqlite3.connect("./20.Proyecto_Python/base.db")

# Crear cursor
cursor = conexion.cursor()

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = str(datetime.datetime.now())

        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        sql = "INSERT INTO usuarios VALUES(null, ?, ?, ?, ?, ?)"
        
        cursor.execute(sql, usuario)
        conexion.commit()

        return [cursor.rowcount, self]


    def identificar(self):
        return self.nombre