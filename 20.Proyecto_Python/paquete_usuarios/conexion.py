
####### Este archivo es para conectarse a la base de datos #######

#import mysql.connector
import sqlite3
"""

 ######## CON MYSQL NO HE PODIDO ########

"""
'''database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Cebanc1920",
    database = "proyecto_python",
    port = 3306
)'''
#cursor = database.cursor(buffered=True)

def conectar():
    # Conexión
    conexion = sqlite3.connect("./20.Proyecto_Python/base.db")

    # Crear cursor
    cursor = conexion.cursor()

    return [conexion, cursor]
