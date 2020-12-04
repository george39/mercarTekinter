import datetime
import hashlib
import conector.conexion as conexion


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]




class Proveedor:

    def __init__(self, nombre, nombre_empresa):        
        self.nombre = nombre
        self.nombre_empresa = nombre_empresa
        


    def registrar(self):
        fecha = datetime.datetime.now()

        
        sql = "INSERT INTO proveedores VALUES(null, %s, %s, %s)"
        proveedor = (self.nombre, self.nombre_empresa, fecha)


        try:
            cursor.execute(sql, proveedor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]    

        return result


    def listar(self):
        sql = "SELECT * FROM  proveedores"

        cursor.execute(sql)
        result = cursor.fetchall()
        proveedor = (self.nombre, self.nombre_empresa)

        return result    