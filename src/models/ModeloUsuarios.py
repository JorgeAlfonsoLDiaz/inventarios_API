from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Usuarios import Usuarios # Se importa la clase Usuarios del módulo entities.Usuarios

class ModeloUsuarios():

    @classmethod
    def get_usuarios(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            usuarios = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, empresa, area, puesto, nombre, apellido_paterno, apellido_materno FROM usuarios WHERE eliminado = false ORDER BY id_usuario DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    usuario = Usuarios(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_usuario(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, empresa, area, puesto, nombre, apellido_paterno, apellido_materno FROM usuarios WHERE eliminado = false AND id_usuario = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                usuario = None
                if resultado != None:
                    usuario = Usuarios(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_usuario(self, usuario):  # Registrar una nueva empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (empresa, area, puesto, nombre, apellido_paterno, apellido_materno)
                                VALUES (%s, %s, %s, %s, %s, %s)""", (usuario.empresa, usuario.area, usuario.puesto, usuario.nombre, usuario.apellido_paterno, usuario.apellido_materno))  # Se ejecuta una inserción en la tabla usuarios
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
        
        
    @classmethod
    def delete_usuario(self, id):  # Eliminar una empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE usuarios SET eliminado = true WHERE id_usuario = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_usuario(self, id, usuario):  # Actualizar una empresa
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuarios SET empresa = %s, area = %s, puesto = %s, nombre = %s, apellido_paterno = %s, apellido_materno = %s
                                WHERE id_usuario = %s AND eliminado = false""", (usuario.empresa, usuario.area, usuario.puesto, usuario.nombre, usuario.apellido_paterno, usuario.apellido_materno, id))  # Se ejecuta una actualización en la tabla empresas
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
