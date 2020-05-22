# Importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect("pruebas.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXIST productos(id int(10) PRIMARY" +
"KEY,AUTOINCREMENT, titulo VARCHAR(200), descripcion TEXT, precio int(255))")


# Cerrar conexión
conexion.close()
