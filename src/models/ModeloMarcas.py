from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Marcas import Marcas # Se importa la clase Marcas del módulo entities.Marcas

class ModeloMarcas():

    @classmethod
    def get_marcas(cls):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            marcas = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_marca, nombre, descripcion FROM marcas WHERE eliminado = false ORDER BY id_marca DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    marca = Marcas(row[0], row[1], row[2])
                    marcas.append(marca.to_JSON())

            connection.close()
            return marcas
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_marca(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_marca, nombre, descripcion FROM marcas WHERE eliminado = false AND id_marca = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                marca = None
                if resultado != None:
                    marca = Marcas(resultado[0], resultado[1], resultado[2])
                    marca = marca.to_JSON()

            connection.close()
            return marca
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_marca(self, marca):  # Registrar una nueva marca
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO marcas (nombre, descripcion)
                                VALUES (%s, %s)""", (marca.nombre, marca.descripcion))  # Se ejecuta una inserción en la tabla marcas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_marca(self, id):  # Eliminar una marca
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE marcas SET eliminado = true WHERE id_marca = %s", (id))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_marca(self, id, marca):  # Actualizar una marca
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE marcas SET nombre = %s, descripcion = %s
                                WHERE id_marca = %s AND eliminado = false""", (marca.nombre, marca.descripcion, id))  # Se ejecuta una actualización en la tabla marcas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
