import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Cebanc1920",
    database = "prueba" # <-- Este parametro es para utilizar esa bd
)

# Cómo saber si la conexion ha sido correcta
print(database)

cursor = database.cursor(buffered=True) # <-- buffered=True para que no falle al ejecutar diferentes consultas

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS prueba")

"""cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICULOS(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
#cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
# Insertar un registro en la tabla
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Ford', 'Fiesta', '15000')")
# Insertas varios registros en la tabla
coches = [
    ('Seat', 'Ibiza', 6000),
    ('Ranault', 'Clio', 5000)
]
cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
#database.commit() # <-- ejecuta el comando

# SELECT y WHERE

cursor.execute("SELECT * FROM vehiculos WHERE precio > 10000 AND marca = 'seat'")
result = cursor.fetchall()

print("Todos los coches -->")
for coche in result:
    print(coche)

print("\n")
cursor.execute("SELECT * FROM vehiculos WHERE marca = 'seat'")
coche = cursor.fetchone()
print("Primer seat -->")
print(coche)

# Borrar registros
cursor.close

cursor2 = database.cursor()
cursor2.execute("DELETE FROM vehiculos")


cursor.execute("INSERT INTO vehiculos VALUES(null, 'Ford', 'Fiesta', '15000')")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Renault', 'Clio', '1000')")
database.commit()

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("Todos los coches -->")
for coche in result:
    print(coche)


cursor2.execute("DELETE FROM vehiculos WHERE marca = 'Ford'")
database.commit()

print(cursor2.rowcount, " Registros Borrados")

# Actualizar columnas
cursor2.execute("UPDATE vehiculos SET modelo = 'Scenic' WHERE modelo = 'Clio'")
database.commit()