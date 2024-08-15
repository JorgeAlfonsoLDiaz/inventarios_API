from flask import Flask, jsonify, request 
from flask_cors import CORS

from config import config  # Se importa el módulo config que permite cargar las configuraciones de la aplicación

# Rutas
from routes import condiciones, categorias, areas, empresas, usuarios, clasificaciones, inventario, marcas  # Se importan los blueprints de las rutas

app = Flask(__name__)  # Se crea la instancia de la aplicación

CORS(app, resources={"*": {"origins": "http://localhost:5173"}})
  # Se puede configurar CORS para la aplicación

def page_not_found(e):  # Función que maneja errores 404
    return jsonify({'message': 'Page not found'}), 404

if __name__ == '__main__':  # Se ejecuta la aplicación 
  
    app.config.from_object(config['development'])  # Se cargan las configuraciones de desarrollo

    app.register_blueprint(inventario.main, url_prefix='/inventarios/inventario')  # Se registra el blueprint del inventario en la aplicación
    app.register_blueprint(condiciones.main, url_prefix='/inventarios/condiciones')  # Se registra el blueprint de las condiciones en la aplicación
    app.register_blueprint(categorias.main, url_prefix='/inventarios/categorias')  # Se registra el blueprint de las categorías en la aplicación
    app.register_blueprint(areas.main, url_prefix='/inventarios/areas')  # Se registra el blueprint de las áreas en la aplicación
    app.register_blueprint(empresas.main, url_prefix='/inventarios/empresas')  # Se registra el blueprint de las empresas en la aplicación
    app.register_blueprint(usuarios.main, url_prefix='/inventarios/usuarios')  # Se registra el blueprint de los usuarios en la aplicación
    app.register_blueprint(clasificaciones.main, url_prefix='/inventarios/clasificaciones')  # Se registra el blueprint de las clasificaciones en la aplicación
    app.register_blueprint(marcas.main, url_prefix='/inventarios/marcas')  # Se registra el blueprint de las marcas en la aplicación

    # Manejadores de errores
    app.register_error_handler(404, page_not_found)  # Se registra la función de manejo de errores 404
    app.run(debug=True)
