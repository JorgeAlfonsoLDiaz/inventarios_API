from flask import Flask, jsonify, request 
from flask_cors import CORS

from config import config  # Se importa el módulo config que permite cargar las configuraciones de la aplicación

# Rutas
from routes import marcas, condiciones, categorias

app = Flask(__name__)  # Se crea la instancia de la aplicación

CORS(app, resources={"*": {"origins": "http://localhost:5173"}})  # Se habilita CORS para la aplicación

def page_not_found(e):  # Función que maneja errores 404
    return jsonify({'message': 'Page not found'}), 404

if __name__ == '__main__':  # Se ejecuta la aplicación 
    app.config.from_object(config['development'])  # Se cargan las configuraciones de desarrollo

    # Blueprints
    app.register_blueprint(marcas.main, url_prefix='/inventarios/marcas')  # Se registra el blueprint de marcas en la aplicación
    app.register_blueprint(condiciones.main, url_prefix='/inventarios/condiciones')  # Se registra el blueprint de condiciones en la aplicación
    app.register_blueprint(categorias.main, url_prefix='/inventarios/categorias')  # Se registra el blueprint de categorías en la aplicación

    # Manejadores de errores
    app.register_error_handler(404, page_not_found)  # Se registra la función de manejo de errores 404
    app.run(debug=True)
