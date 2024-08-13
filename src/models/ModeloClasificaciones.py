from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Clasificaciones import Clasificaciones # Se importa la clase Clasificaciones del módulo entities.Clasiificaciones

class ModeloClasificaciones():

    @classmethod
    def get_clasificaciones(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            clasificaciones = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_clasificacion, categoria, nombre, descripcion, estatus FROM clasificaciones WHERE eliminado = false ORDER BY id_clasificacion DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    clasificacion = Clasificaciones(row[0], row[1], row[2], row[3], row[4])
                    clasificaciones.append(clasificacion.to_JSON())

            connection.close()
            return clasificaciones
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_clasificacion(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_clasificacion, categoria, nombre, descripcion, estatus FROM clasificaciones WHERE eliminado = false AND id_clasificacion = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                clasificacion = None
                if resultado != None:
                    clasificacion = Clasificaciones(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                    clasificacion = clasificacion.to_JSON()

            connection.close()
            return clasificacion
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_clasificacion(self, clasificacion):  # Registrar una nueva clasificación
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO clasificaciones (categoria, nombre, descripcion, estatus)
                                VALUES (%s, %s, %s, %s)""", (clasificacion.categoria, clasificacion.nombre, clasificacion.descripcion, clasificacion.estatus))  # Se ejecuta una inserción en la tabla clasificaciones
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_clasificacion(self, id):  # Eliminar una clasificación
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE clasificaciones SET eliminado = true WHERE id_clasificacion = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_clasificacion(self, id, clasificacion):  # Actualizar una clasificación
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE clasificaciones SET categoria = %s, nombre = %s, descripcion = %s, estatus = %s
                                WHERE id_clasificacion = %s AND eliminado = false""", (clasificacion.categoria, clasificacion.nombre, clasificacion.descripcion, clasificacion.estatus, id))  # Se ejecuta una actualización en la tabla clasificaciones
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
