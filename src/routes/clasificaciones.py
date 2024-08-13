from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Clasificaciones import Clasificaciones  # Se importa la entity

# Modelos
from models.ModeloClasificaciones import ModeloClasificaciones # Se importa el modelo

# Schema
from models.schemas.schema import ClasificacionSchema  # Se importa el schema



main = Blueprint('clasificaciones_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'clasificaciones_blueprint'

# Aquí van las rutas correspondientes a la entidad Clasificaciones   |
#                                                                    |
#                                                                    V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/clasificaciones' con el método GET
def get_clasificaciones():
    try:
        clasificaciones = ModeloClasificaciones.get_clasificaciones()  # Se obtienen los resultados
        return jsonify(clasificaciones), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/clasificaciones' con el método GET (con un path parameter)
def get_clasificacion(id):
    try:
        clasificacion = ModeloClasificaciones.get_clasificacion(id)  # Se obtienen los resultados

        if clasificacion != None:
            return jsonify(clasificacion), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/clasificaciones' con el método POST
def create_clasificaciones():
    try:
        # Validación
        clasificacion_schema = ClasificacionSchema()
        datos_validados = clasificacion_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        clasificacion = Clasificaciones(id_clasificacion=None, categoria=datos_validados['categoria'], nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloClasificaciones.create_clasificacion(clasificacion)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Clasificación registrada correctamente', 'Registro': clasificacion.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/clasificaciones' con el método PUT (para eliminar)
def delete_clasificaciones(id):
    try: 
        filas_afectadas = ModeloClasificaciones.delete_clasificacion(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Clasificación eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/clasificaciones' con el método PUT
def update_clasificaciones(id):
    try:
        # Validación
        clasificacion_schema = ClasificacionSchema()
        datos_validados = clasificacion_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        clasificacion = Clasificaciones(id_clasificacion=None, categoria=datos_validados['categoria'], nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloClasificaciones.update_clasificacion(id, clasificacion)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Clasificación actualizada correctamente', 'Registro': clasificacion.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500