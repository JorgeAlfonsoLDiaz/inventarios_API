from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Empresas import Empresas # Se importa la clase Empresas del módulo entities.Empresas

class ModeloEmpresas():

    @classmethod
    def get_empresas(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            empresas = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_empresa, nombre, nombre_corto, director_general, descripcion, estatus FROM empresas WHERE eliminado = false ORDER BY id_empresa DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    empresa = Empresas(row[0], row[1], row[2], row[3], row[4], row[5])
                    empresas.append(empresa.to_JSON())

            connection.close()
            return empresas
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_empresa(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_empresa, nombre, nombre_corto, director_general, descripcion, estatus FROM empresas WHERE eliminado = false AND id_empresa = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                empresa = None
                if resultado != None:
                    empresa = Empresas(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                    empresa = empresa.to_JSON()

            connection.close()
            return empresa
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_empresa(self, empresa):  # Registrar una nueva empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO empresas (nombre, nombre_corto, director_general, descripcion, estatus)
                                VALUES (%s, %s, %s, %s, %s)""", (empresa.nombre, empresa.nombre_corto, empresa.director_general, empresa.descripcion, empresa.estatus))  # Se ejecuta una inserción en la tabla empresas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_empresa(self, id):  # Eliminar una empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE empresas SET eliminado = true WHERE id_empresa = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_empresa(self, id, empresa):  # Actualizar una empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE empresas SET nombre = %s, nombre_corto = %s, director_general = %s, descripcion = %s, estatus = %s
                                WHERE id_empresa = %s AND eliminado = false""", (empresa.nombre, empresa.nombre_corto, empresa.director_general, empresa.descripcion, empresa.estatus, id))  # Se ejecuta una actualización en la tabla empresas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
