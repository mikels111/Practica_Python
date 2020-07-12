import paquete_usuarios.conexion as moduloConexion
import datetime
import hashlib


connect = moduloConexion.conectar()
conexion = connect[0]
cursor = connect[1]


class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = str(datetime.datetime.now())

        # cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) 

        sql = "INSERT INTO usuarios VALUES(null, ?, ?, ?, ?, ?)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            conexion.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result


    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = ? AND password = ?"

        # cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result