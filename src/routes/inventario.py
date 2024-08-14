from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Inventario import Inventario  # Se importa la entity

# Modelos
from models.ModeloInventario import ModeloInventario # Se importa el modelo

# Schema
from models.schemas.schema import InventarioSchema  # Se importa el schema



main = Blueprint('inventario_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'inventario_blueprint'

# Aquí van las rutas correspondientes a la entidad Inventario        |
#                                                                    |
#                                                                    V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/inventario' con el método GET
def get_articulos():
    try:
        articulos = ModeloInventario.get_articulos()  # Se obtienen los resultados
        return jsonify(articulos), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/inventario' con el método GET (con un path parameter)
def get_articulo(id):
    try:
        articulo = ModeloInventario.get_articulo(id)  # Se obtienen los resultados

        if articulo != None:
            return jsonify(articulo), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/inventario' con el método POST
def create_articulos():
    try:
        # Validación
        articulo_schema = InventarioSchema()
        datos_validados = articulo_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        articulo = Inventario(id_articulo=None, usuario_asignado=datos_validados.get('usuario_asignado'), clasificacion=datos_validados.get('clasificacion'), marca=datos_validados.get('marca'), condicion=datos_validados.get('condicion'), no_serie=datos_validados.get('no_serie'), modelo=datos_validados.get('modelo'), fecha_asignacion=None, cantidad=datos_validados.get('cantidad'), otras_especificaciones=datos_validados.get('otras_especificaciones'))  # Nueva entidad con los datos de la solicitud. Utilizar método .get() para evitar errores por campos faltantes
        filas_afectadas = ModeloInventario.create_articulo(articulo)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Artículo registrado correctamente', 'Registro': articulo.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/inventario' con el método PUT (para eliminar)
def delete_articulos(id):
    try: 
        filas_afectadas = ModeloInventario.delete_articulo(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Artículo eliminado temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/inventario' con el método PUT
def update_articulos(id):
    try:
        # Validación
        articulo_schema = InventarioSchema()
        datos_validados = articulo_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        articulo = Inventario(id_articulo=None, usuario_asignado=datos_validados.get('usuario_asignado'), clasificacion=datos_validados.get('clasificacion'), marca=datos_validados.get('marca'), condicion=datos_validados.get('condicion'), no_serie=datos_validados.get('no_serie'), modelo=datos_validados.get('modelo'), fecha_asignacion=None, cantidad=datos_validados.get('cantidad'), otras_especificaciones=datos_validados.get('otras_especificaciones'))  # Nueva entidad con los datos de la solicitud. Utilizar método .get() para evitar errores por campos faltantes        
        filas_afectadas = ModeloInventario.update_articulo(id, articulo)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Artículo actualizado correctamente', 'Registro': articulo.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/listar', methods=['GET'])  # Se define una ruta para la URI '/inventario' con el método GET
def listar_articulos():
    try:
        articulos = ModeloInventario.listar_articulos()  # Se obtienen los resultados
        return jsonify(articulos), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
