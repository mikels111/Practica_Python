# Importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect("pruebas.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo VARCHAR(200),
descripcion TEXT,
precio int(255)
)""")

# Guardar cambios
conexion.commit()

# Insertar Datos
cursor.execute("INSERT INTO productos VALUES(null, 'primer producto','descripcion producto', 550)")
conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos resgistros
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono Movil", "Buen telefono", 500),
    ("Placa base", "Buen Placa", 300),
    ("tablet", "Buen tablet", 600),
]
cursor.executemany("INSERT INTO productos VALUES(null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 525  WHERE precio = 500")

# Lectura de datos
cursor.execute("SELECT * FROM productos WHERE precio > 300")
productos = cursor.fetchall()
for producto in productos:
    print("id", producto[0])
    print("nombre del producto: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT descripcion FROM productos")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()
