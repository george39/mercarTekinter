
CREATE DATABASE IF NOT EXISTS supermercado;
use supermercado;





CREATE TABLE proveedores(
    id              int(25) auto_increment not null,    
    nombre          varchar(255) not null,
    nombre_empresa  varchar(255) not null,    
    fecha           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT      pk_productos PRIMARY KEY(id)    
)ENGINE = InnoDb;


CREATE TABLE productos(
    id              int(25) auto_increment not null,
    proveedor_id    int(25) not null,
    nombre          varchar(255) not null,
    precio          int(25) not null,
    cantidad        int(25) not null,
    fecha           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT      pk_productos PRIMARY KEY(id),
    CONSTRAINT      fk_productos FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)  
)ENGINE = InnoDb;



