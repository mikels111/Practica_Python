CREATE DATABASE IF NOT EXISTS proyecto_python;
use proyecto_python;
CREATE TABLE usuarios(
id          int(25) auto_increment not null,
nombre      VARCHAR(100),
apellidos   VARCHAR(255),
email       VARCHAR(255) not null,
password    VARCHAR(255) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
id INT(25) auto_increment NOT NULL,
usuario_id INT(25) NOT NULL,
titulo VARCHAR(255) NOT NULL,
descripcion MEDIUMTEXT,
fecha date NOT NULL,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;


