from flask import Blueprint, jsonify, request # Se importan las clases Blueprint, jsonify y request de Flask

# Validación
from marshmallow import ValidationError

# Entities
from models.entities.Usuarios import Usuarios  # Se importa la entity

# Modelos
from models.ModeloUsuarios import ModeloUsuarios # Se importa el modelo

# Schema
from models.schemas.schema import UsuarioSchema  # Se importa el schema



main = Blueprint('usuarios_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'usuarios_blueprint'

# Aquí van las rutas correspondientes a la entidad Usuarios   |
#                                                             |
#                                                             V

@main.route('/', methods=['GET'])  # Se define una ruta para la URI '/usuarios' con el método GET
def get_usuarios():
    try:
        usuarios = ModeloUsuarios.get_usuarios()  # Se obtienen los resultados
        return jsonify(usuarios), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/<id>', methods=['GET'])  # Se define una ruta para la URI '/usuarios' con el método GET (con un path parameter)
def get_usuario(id):
    try:
        usuario = ModeloUsuarios.get_usuario(id)  # Se obtienen los resultados

        if usuario != None:
            return jsonify(usuario), 200  # Retorna un objeto JSON usando jsonify
        else:
            return jsonify({'message': 'Registro no encontrado'}), 404  # No encontró el registro
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500



@main.route('/crear', methods=['POST'])  # Se define una ruta para la URI '/usuarios' con el método POST
def create_usuarios():
    try:
        # Validación
        usuario_schema = UsuarioSchema()
        datos_validados = usuario_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        usuario = Usuarios(id_usuario=None, empresa=datos_validados['empresa'], area=datos_validados['area'], puesto=datos_validados['puesto'], nombre=datos_validados['nombre'], apellido_paterno=datos_validados['apellido_paterno'], apellido_materno=datos_validados['apellido_materno'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloUsuarios.create_usuario(usuario)  # Se crea el registro

        return jsonify({'filas_afectadas': filas_afectadas,'message': 'Usuario registrado correctamente', 'Registro': usuario.to_JSON() }), 201  # Confirma la inserción del registro
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/eliminar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/usuarios' con el método PUT (para eliminar)
def delete_usuarios(id):
    try: 
        filas_afectadas = ModeloUsuarios.delete_usuario(id)  # Elimina temporalmente el registro

        if filas_afectadas == 1:
            return jsonify({'message': 'Usuario eliminado temporalmente', 'ID_registro': str(id) }), 200  # Confirma la eliminación temporal del registro

        else:
            return jsonify({'message': 'Registro no encontrado'}), 404


    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
    


@main.route('/actualizar/<id>', methods=['PUT'])  # Se define una ruta para la URI '/usuarios' con el método PUT
def update_usuarios(id):
    try:
        # Validación
        usuario_schema = UsuarioSchema()
        datos_validados = usuario_schema.load(request.json)  # Se validan los datos de la petición

        # Si se validan: 
        usuario = Usuarios(id_usuario=None, empresa=datos_validados['empresa'], area=datos_validados['area'], puesto=datos_validados['puesto'], nombre=datos_validados['nombre'], apellido_paterno=datos_validados['apellido_paterno'], apellido_materno=datos_validados['apellido_materno'])  # Nueva entidad con los datos de la solicitud
        filas_afectadas = ModeloUsuarios.update_usuario(id, usuario)  # Se actualiza el registro

        if filas_afectadas == 1:
            return jsonify({'filas_afectadas': filas_afectadas, 'message': 'Usuario actualizado correctamente', 'Registro': usuario.to_JSON() }), 200  # Confirma la actualización del registro
        
        else: 
            return jsonify({'message': 'No se han actualizado registros'}), 404

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500