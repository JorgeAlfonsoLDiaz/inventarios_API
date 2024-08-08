from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Marcas import Marcas # Se importa la clase Marcas del módulo entities.Marcas

class ModeloMarcas():

    @classmethod
    def get_marcas(self):
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            marcas = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute('SELECT id_marca, nombre, descripcion FROM marcas WHERE eliminado = false') # Se ejecuta una consulta para obtener todas las marcas que no han sido eliminadas
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    marca = Marcas(row[0], row[1], row[2])
                    marcas.append(marca.to_JSON())

            connection.close()
            return marcas
        
        except Exception as e:
            raise Exception(e)
