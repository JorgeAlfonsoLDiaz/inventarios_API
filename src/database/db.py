import psycopg2  # Adaptador para bases de datos PostgreSQL
from psycopg2 import DatabaseError
from decouple import config  # Para las variables de entorno configuradas

def get_connection():  # Realiza la conexión a la base de datos utilizando las variables de entorno de la configuración

    try:
        return psycopg2.connect(host=config('PGSQL_HOST'), user=config('PGSQL_USER'), password=config('PGSQL_PASSWORD'), database=config('PGSQL_DATABASE'))
    except DatabaseError as error:
        raise error
    
