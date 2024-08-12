from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Condiciones import Condiciones # Se importa la clase Condiciones del módulo entities.Condiciones

class ModeloCondiciones():

    @classmethod
    def get_condiciones(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            condiciones = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_condicion, condicion, descripcion FROM condiciones WHERE eliminado = false ORDER BY id_condicion DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    condicion = Condiciones(row[0], row[1], row[2])
                    condiciones.append(condicion.to_JSON())

            connection.close()
            return condiciones
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_condicion(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_condicion, condicion, descripcion FROM condiciones WHERE eliminado = false AND id_condicion = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                condicion = None
                if resultado != None:
                    condicion = Condiciones(resultado[0], resultado[1], resultado[2])
                    condicion = condicion.to_JSON()

            connection.close()
            return condicion
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_condicion(self, condicion):  # Registrar una nueva condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO condiciones (condicion, descripcion)
                                VALUES (%s, %s)""", (condicion.condicion, condicion.descripcion))  # Se ejecuta una inserción en la tabla condiciones
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_condicion(self, id):  # Eliminar una condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE condiciones SET eliminado = true WHERE id_condicion = %s", (id))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_condicion(self, id, condicion):  # Actualizar una condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE condiciones SET condicion = %s, descripcion = %s
                                WHERE id_condicion = %s AND eliminado = false""", (condicion.condicion, condicion.descripcion, id))  # Se ejecuta una actualización en la tabla condiciones
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
