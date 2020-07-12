
####### Este archivo es para crear la base de datos #######

# Importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect("./20.Proyecto_Python/base.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
usuarios(
id INTEGER PRIMARY KEY AUTOINCREMENT not null,
nombre VARCHAR(200),
apellidos VARCHAR(200),
email VARCHAR(255),
password VARCHAR(255),
fecha date not null,
CONSTRAINT uq_email UNIQUE(email)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
notas(
id INTEGER PRIMARY KEY AUTOINCREMENT not null,
usuario_id INTEGER NOT NULL,
titulo VARCHAR(255) NOT NULL,
descripcion VARCHAR(255),
fecha date NOT NULL
)""")


# Guardar cambios
conexion.commit()