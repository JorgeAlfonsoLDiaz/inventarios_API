from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Condiciones import Condiciones  # Se importa la entity

# Modelos
from models.ModeloCondiciones import ModeloCondiciones # Se importa el modelo

# Schema
from models.schemas.schema import CondicionSchema  # Se importa el schema



main = Blueprint('condiciones_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'marcas_blueprint'

# Aquí van las rutas correspondientes a la entidad Marcas  |
#                                                          |
#                                                          V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/condiciones' con el método GET
def get_condiciones():
    try:
        condiciones = ModeloCondiciones.get_condiciones()  # Se obtienen los resultados
        return jsonify(condiciones), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/condiciones' con el método GET (con un path parameter)
def get_condicion(id):
    try:
        condicion = ModeloCondiciones.get_condicion(id)  # Se obtienen los resultados

        if condicion != None:
            return jsonify(condicion), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/condiciones' con el método POST
def create_condiciones():
    try:
        # Validación
        condicion_schema = CondicionSchema()
        datos_validados = condicion_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        condicion = Condiciones(id_condicion=None, condicion=datos_validados['condicion'], descripcion=datos_validados['descripcion'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloCondiciones.create_condicion(condicion)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Condición registrada correctamente', 'Registro': condicion.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/condiciones' con el método PUT (para eliminar)
def delete_condiciones(id):
    try: 
        filas_afectadas = ModeloCondiciones.delete_condicion(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Condición eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/condiciones' con el método PUT
def update_condiciones(id):
    try:
        # Validación
        condicion_schema = CondicionSchema()
        datos_validados = condicion_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        condicion = Condiciones(id_condicion=None, condicion=datos_validados['condicion'], descripcion=datos_validados['descripcion'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloCondiciones.update_condicion(id, condicion)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Condición actualizada correctamente', 'Registro': condicion.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500