import datetime
import hashlib
import conector.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]




class Producto:

    def __init__(self, proveedor_id, nombre, precio, cantidad):
        self.proveedor_id = proveedor_id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        


    def registrar(self):
        fecha = datetime.datetime.now()

        
        sql = "INSERT INTO productos VALUES(null, %s, %s, %s, %s)"
        producto = (self.proveedor_id, self.nombre, self.precio, self.cantidad)


        try:
            cursor.execute(sql, producto)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]    

        return result