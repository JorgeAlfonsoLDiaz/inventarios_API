from flask import Blueprint, jsonify # Se importan las clases Blueprint y jsonify de Flask

# Modelos
from models.ModeloMarcas import ModeloMarcas # Se importa la clase ModeloMarcas del módulo models.modeloMarcas


main = Blueprint('marcas_blueprint', __name__)   # Se crea una instancia de Blueprint con el nombre 'marcas_blueprint'

@main.route('/marcas', methods=['GET'])  # Se define una ruta para la URI '/marcas' con el método GET
def get_marcas():
    try:
        marcas = ModeloMarcas.get_marcas()  # Se obtienen los resultados
        return jsonify(marcas), 200  # Retorna un objeto JSON usando jsonify
    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Retorna un mensaje de error 500
