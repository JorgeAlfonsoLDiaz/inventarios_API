from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Areas import Areas # Se importa la clase Categorias del módulo entities.Categorias

class ModeloAreas():

    @classmethod
    def get_areas(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            areas = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_area, nombre, descripcion, estatus FROM areas WHERE eliminado = false ORDER BY id_area DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    area = Areas(row[0], row[1], row[2], row[3])
                    areas.append(area.to_JSON())

            connection.close()
            return areas
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_area(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_area, nombre, descripcion, estatus FROM areas WHERE eliminado = false AND id_area = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                area = None
                if resultado != None:
                    area = Areas(resultado[0], resultado[1], resultado[2], resultado[3])
                    area = area.to_JSON()

            connection.close()
            return area
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_area(self, area):  # Registrar una nueva área
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO areas (nombre, descripcion, estatus)
                                VALUES (%s, %s, %s)""", (area.nombre, area.descripcion, area.estatus))  # Se ejecuta una inserción en la tabla areas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_area(self, id):  # Eliminar una categoría
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE areas SET eliminado = true WHERE id_area = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_area(self, id, area):  # Actualizar una condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE areas SET nombre = %s, descripcion = %s, estatus = %s
                                WHERE id_area = %s AND eliminado = false""", (area.nombre, area.descripcion, area.estatus, id))  # Se ejecuta una actualización en la tabla areas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
