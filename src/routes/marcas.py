from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Marcas import Marcas  # Se importa la entity

# Modelos
from models.ModeloMarcas import ModeloMarcas # Se importa el modelo

# Schema
from models.schemas.schema import MarcaSchema  # Se importa el schema



main = Blueprint('marcas_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'marcas_blueprint'

# Aquí van las rutas correspondientes a la entidad Marcas        |
#                                                                |
#                                                                V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/marcas' con el método GET
def get_marcas():
    try:
        marcas = ModeloMarcas.get_marcas()  # Se obtienen los resultados
        return jsonify(marcas), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/marcas' con el método GET (con un path parameter)
def get_marca(id):
    try:
        marca = ModeloMarcas.get_marca(id)  # Se obtienen los resultados

        if marca != None:
            return jsonify(marca), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/marcas' con el método POST
def create_marcas():
    try:
        # Validación
        marca_schema = MarcaSchema()
        datos_validados = marca_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        marca = Marcas(id_marca=None, nombre=datos_validados.get('nombre'), descripcion=datos_validados.get('descripcion'))  # Nueva entidad con los datos de la solicitud. Utilizar método .get() para evitar errores por campos faltantes
        filas_afectadas = ModeloMarcas.create_marca(marca)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Marca registrada correctamente', 'Registro': marca.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500



@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/marcas' con el método PUT (para eliminar)
def delete_marcas(id):
    try: 
        filas_afectadas = ModeloMarcas.delete_marca(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Marca eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/marcas' con el método PUT
def update_marcas(id):
    try:
        # Validación
        marca_schema = MarcaSchema()
        datos_validados = marca_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        marca = Marcas(id_marca=None, nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloMarcas.update_marca(id, marca)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Marca actualizada correctamente', 'Registro': marca.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500