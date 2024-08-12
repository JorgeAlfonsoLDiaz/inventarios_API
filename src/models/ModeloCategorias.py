from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Categorias import Categorias # Se importa la clase Categorias del módulo entities.Categorias

class ModeloCategorias():

    @classmethod
    def get_categorias(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            categorias = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_categoria, nombre, descripcion, estatus FROM categorias WHERE eliminado = false ORDER BY id_categoria DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    categoria = Categorias(row[0], row[1], row[2], row[3])
                    categorias.append(categoria.to_JSON())

            connection.close()
            return categorias
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_categoria(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_categoria, nombre, descripcion, estatus FROM categorias WHERE eliminado = false AND id_categoria = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                categoria = None
                if resultado != None:
                    categoria = Categorias(resultado[0], resultado[1], resultado[2], resultado[3])
                    categoria = categoria.to_JSON()

            connection.close()
            return categoria
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_categoria(self, categoria):  # Registrar una nueva condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO categorias (nombre, descripcion, estatus)
                                VALUES (%s, %s, %s)""", (categoria.nombre, categoria.descripcion, categoria.estatus))  # Se ejecuta una inserción en la tabla categorias
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_categoria(self, id):  # Eliminar una categoría
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE categorias SET eliminado = true WHERE id_categoria = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_categoria(self, id, categoria):  # Actualizar una condición
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE categorias SET nombre = %s, descripcion = %s, estatus = %s
                                WHERE id_categoria = %s AND eliminado = false""", (categoria.nombre, categoria.descripcion, categoria.estatus, id))  # Se ejecuta una actualización en la tabla categorias
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
