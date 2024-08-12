from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Areas import Areas  # Se importa la entity

# Modelos
from models.ModeloAreas import ModeloAreas # Se importa el modelo

# Schema
from models.schemas.schema import AreaSchema  # Se importa el schema



main = Blueprint('areas_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'areas_blueprint'

# Aquí van las rutas correspondientes a la entidad Areas   |
#                                                          |
#                                                          V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/areas' con el método GET
def get_areas():
    try:
        areas = ModeloAreas.get_areas()  # Se obtienen los resultados
        return jsonify(areas), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/areas' con el método GET (con un path parameter)
def get_area(id):
    try:
        area = ModeloAreas.get_area(id)  # Se obtienen los resultados

        if area != None:
            return jsonify(area), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/areas' con el método POST
def create_areas():
    try:
        # Validación
        area_schema = AreaSchema()
        datos_validados = area_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        area = Areas(id_area=None, nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloAreas.create_area(area)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Área registrada correctamente', 'Registro': area.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/areas' con el método PUT (para eliminar)
def delete_areas(id):
    try: 
        filas_afectadas = ModeloAreas.delete_area(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Área eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/areas' con el método PUT
def update_areas(id):
    try:
        # Validación
        area_schema = AreaSchema()
        datos_validados = area_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        area = Areas(id_area=None, nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloAreas.update_area(id, area)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Área actualizada correctamente', 'Registro': area.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500