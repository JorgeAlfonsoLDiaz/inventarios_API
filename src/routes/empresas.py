from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Empresas import Empresas  # Se importa la entity

# Modelos
from models.ModeloEmpresas import ModeloEmpresas # Se importa el modelo

# Schema
from models.schemas.schema import EmpresaSchema  # Se importa el schema



main = Blueprint('empresas_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'empresas_blueprint'

# Aquí van las rutas correspondientes a la entidad Empresas   |
#                                                             |
#                                                             V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/empresas' con el método GET
def get_empresas():
    try:
        empresas = ModeloEmpresas.get_empresas()  # Se obtienen los resultados
        return jsonify(empresas), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/empresas' con el método GET (con un path parameter)
def get_empresa(id):
    try:
        empresa = ModeloEmpresas.get_empresa(id)  # Se obtienen los resultados

        if empresa != None:
            return jsonify(empresa), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/empresas' con el método POST
def create_empresas():
    try:
        # Validación
        empresa_schema = EmpresaSchema()
        datos_validados = empresa_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        empresa = Empresas(id_empresa=None, nombre=datos_validados['nombre'], nombre_corto=datos_validados['nombre_corto'], director_general=datos_validados['director_general'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloEmpresas.create_empresa(empresa)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Empresa registrada correctamente', 'Registro': empresa.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/empresas' con el método PUT (para eliminar)
def delete_areas(id):
    try: 
        filas_afectadas = ModeloEmpresas.delete_empresa(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Empresa eliminada temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/empresas' con el método PUT
def update_empresas(id):
    try:
        # Validación
        empresa_schema = EmpresaSchema()
        datos_validados = empresa_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        empresa = Empresas(id_empresa=None, nombre=datos_validados['nombre'], nombre_corto=datos_validados['nombre_corto'], director_general=datos_validados['director_general'], descripcion=datos_validados['descripcion'], estatus=datos_validados['estatus'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloEmpresas.update_empresa(id, empresa)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Empresa actualizada correctamente', 'Registro': empresa.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500