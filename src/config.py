from decouple import config  # Decouple permite gestionar y cargar las variables de entorno, y config se utiliza para obtener valores de configuración

class Config:  # Clase que contiene configuraciones comunes para la aplicación Flask
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):  # Sublase de Config que contiene configuraciones específicas para el entorno de desarrollo
    DEBUG = True

config = {
    'development': DevelopmentConfig,
}  # Mapea los nombres de entornos a sus clases de configuración correspondientes
