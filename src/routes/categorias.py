from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Categorias import Categorias  # Se importa la entity

# Modelos
from models.ModeloCategorias import ModeloCategorias # Se importa el modelo

# Schema
from models.schemas.schema import CategoriaSchema  # Se importa el schema



main = Blueprint('categorias_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'marcas_blueprint'

# Aquí van las rutas correspondientes a la entidad Marcas  |
#                                                          |
#                                                          V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/categorias' con el método GET
def get_categorias():
    try:
        categorias = ModeloCategorias.get_categorias()  # Se obtienen los resultados
        return jsonify(categorias), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/categorias' con el método GET (con un path parameter)
def get_categoria(id):
    try:
        categoria = ModeloCategorias.get_categoria(id)  # Se obtienen los resultados

        if categoria != None:
            return jsonify(categoria), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/categorias' con el método POST
def create_categorias():
    try:
        # Validación
        categoria_schema = CategoriaSchema()
        datos_validados = categoria_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        categoria = Categorias(id_categoria=None, nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloCategorias.create_categoria(categoria)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Categoría registrada correctamente', 'Registro': categoria.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/categorias' con el método PUT (para eliminar)
def delete_categorias(id):
    try: 
        filas_afectadas = ModeloCategorias.delete_categoria(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Categoría eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/categorias' con el método PUT
def update_categorias(id):
    try:
        # Validación
        categoria_schema = CategoriaSchema()
        datos_validados = categoria_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        categoria = Categorias(id_categoria=None, nombre=datos_validados['nombre'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloCategorias.update_categoria(id, categoria)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Categoría actualizada correctamente', 'Registro': categoria.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500