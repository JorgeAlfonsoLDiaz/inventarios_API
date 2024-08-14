from database.db import get_connection # Se importa la función get_connection del módulo db
from .entities.Inventario import Inventario # Se importa la clase Inventario del módulo entities.Inventario
from .entities.InventarioLista import InventarioLista # Se importa la clase InventarioLista del módulo entities.InventarioLista

class ModeloInventario():

    @classmethod
    def get_articulos(self):  # Consultar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            articulos = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_articulo, usuario_asignado, clasificacion, marca, condicion, no_serie, modelo, fecha_asignacion, cantidad, otras_especificaciones FROM inventario WHERE eliminado = false ORDER BY id_articulo DESC") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    articulo = Inventario(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    articulos.append(articulo.to_JSON())

            connection.close()
            return articulos
        
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def get_articulo(self, id):  # Consultar un registro por ID (no eliminado)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_articulo, usuario_asignado, clasificacion, marca, condicion, no_serie, modelo, fecha_asignacion, cantidad, otras_especificaciones FROM inventario WHERE eliminado = false AND id_articulo = %s", (id, )) # Se ejecuta una consulta para obtener el registro especificado (y que no ha sido eliminado)
                resultado = cursor.fetchone()  # Se obtiene el resultado de la consulta

                articulo = None
                if resultado != None:
                    articulo = Inventario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9])
                    articulo = articulo.to_JSON()

            connection.close()
            return articulo
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create_articulo(self, articulo):  # Registrar un nuevo artículo
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                if articulo.usuario_asignado != None:
                    cursor.execute("""INSERT INTO inventario (usuario_asignado, clasificacion, marca, condicion, no_serie, modelo, fecha_asignacion, cantidad, otras_especificaciones)
                                    VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE, %s, %s)""", (articulo.usuario_asignado, articulo.clasificacion, articulo.marca, articulo.condicion, articulo.no_serie, articulo.modelo, articulo.cantidad, articulo.otras_especificaciones))  # Se ejecuta una inserción en la tabla inventario con la fecha actual, sólo si se insertó un usuario
                else:
                    cursor.execute("""INSERT INTO inventario (clasificacion, marca, condicion, no_serie, modelo, cantidad, otras_especificaciones)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s)""", (articulo.clasificacion, articulo.marca, articulo.condicion, articulo.no_serie, articulo.modelo, articulo.cantidad, articulo.otras_especificaciones))  # Se ejecuta una inserción en la tabla inventario sin fecha de asignación, pues no hay usuario asignado
                
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception({"error en el modelo": e})
        
        
    @classmethod
    def delete_articulo(self, id):  # Eliminar un articulo
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                cursor.execute("UPDATE inventario SET eliminado = true WHERE id_articulo = %s", (id, ))  # Se ejecuta una eliminación lógica en la tabla
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)


    @classmethod
    def update_articulo(self, id, articulo):  # Actualizar un artículo
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos

            with connection.cursor() as cursor:
                if articulo.usuario_asignado != None:
                    cursor.execute("""UPDATE inventario SET usuario_asignado = %s, clasificacion = %s, marca = %s, condicion = %s, no_serie = %s, modelo = %s, fecha_asignacion = CURRENT_DATE, cantidad = %s, otras_especificaciones = %s
                                WHERE id_articulo = %s AND eliminado = false""", (articulo.usuario_asignado, articulo.clasificacion, articulo.marca, articulo.condicion, articulo.no_serie, articulo.modelo, articulo.cantidad, articulo.otras_especificaciones, id))  # Se ejecuta una actualización en la tabla inventario con la fecha actual, sólo si se actualizó un usuario
                else:
                    cursor.execute("""UPDATE inventario SET usuario_asignado = NULL, clasificacion = %s, marca = %s, condicion = %s, no_serie = %s, modelo = %s, fecha_asignacion = NULL, cantidad = %s, otras_especificaciones = %s
                                WHERE id_articulo = %s AND eliminado = false""", (articulo.clasificacion, articulo.marca, articulo.condicion, articulo.no_serie, articulo.modelo, articulo.cantidad, articulo.otras_especificaciones, id))
                
                filas_afectadas = cursor.rowcount
                connection.commit()  # Se confirma la operación

            connection.close()
            return filas_afectadas
        
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def listar_articulos(self):  # Listar todos los registros (no eliminados)
        try: 
            connection = get_connection()  # Se ejecuta la función get_connection para obtener una conexión a la base de datos
            articulos = []  # Aquí se almacenan los resultados finales

            with connection.cursor() as cursor:
                cursor.execute("""SELECT 
                                    i.id_articulo,
                                    u.nombre AS usuario_nombre,
                                    u.apellido_paterno AS usuario_apellido_paterno,
                                    u.apellido_materno AS usuario_apellido_materno,
                                    u.puesto AS puesto,
                                    i.fecha_asignacion,
                                    c.nombre AS tipo,
                                    m.nombre AS marca,
                                    i.modelo,
                                    co.condicion AS condicion,
                                    i.cantidad
                                FROM 
                                    inventario i
                                LEFT JOIN 
                                    usuarios u ON i.usuario_asignado = u.id_usuario
                                JOIN 
                                    clasificaciones c ON i.clasificacion = c.id_clasificacion
                                JOIN 
                                    marcas m ON i.marca = m.id_marca
                                JOIN 
                                    condiciones co ON i.condicion = co.id_condicion
                                WHERE
                                    i.eliminado = false;""") # Se ejecuta una consulta para obtener todos los registros que no han sido eliminados
                resultado = cursor.fetchall()  # Se obtienen los resultados de la consulta

                for row in resultado:
                    nombre_completo = f"{row[1] or ''} {row[2] or ''} {row[3] or ''}".strip()
                    articulo = InventarioLista(
                    id_articulo=row[0],
                    usuario_asignado=nombre_completo,
                    puesto=row[4],
                    fecha_asignacion=row[5],
                    tipo=row[6],
                    marca=row[7],
                    modelo=row[8],
                    condicion=row[9],
                    cantidad=row[10]
                )  # Se crea una nueva entidad de esta manera, evitando tener errores por valores vacíos
                    articulos.append(articulo.to_JSON())

            connection.close()
            return articulos
        
        except Exception as e:
            raise Exception(e)
