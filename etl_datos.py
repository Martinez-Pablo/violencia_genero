
import pandas as pd
import pymysql
import glob
from sqlalchemy import create_engine

# Datos necesarios para la conexión a la base de datos
usuario = 'root'
contraseña = 'PabloMartinez1'
nombre_bd = 'victimas_violencia'
host = 'localhost'

# Realizamos la conexión con MySQL
conexion = pymysql.connect(host=host, user=usuario, password=contraseña, db=nombre_bd)
print('conexión establecida con exito')

# Crea un motor SQLAlchemy para la conexión a MySQL
engine = create_engine(f'mysql+pymysql://{usuario}:{contraseña}@{host}/{nombre_bd}')
print('motor creado')

# Nombre de la tabla en la que deseas cargar los datos
nombre_tabla = 'tabla_violencia'

# Lista de nombres de archivos que se cargarán en la base de datos
archivos = glob.glob('linea_144_dataset/*.csv')

for archivo in archivos:
    # Lee el archivo CSV en un DataFrame
    victimas = pd.read_csv(archivo)

    # Convertimos la columna de fecha en datos de tipo fecha
    victimas['fecha'] = pd.to_datetime(victimas['fecha'])

    # Reemplazar los valores vacíos por 0 en la columna edad
    victimas['edad_persona_en_situacion_de_violencia'].fillna(0, inplace=True)

    # Convertimos la columna a tipo entero
    victimas['edad_persona_en_situacion_de_violencia'] = victimas['edad_persona_en_situacion_de_violencia'].astype(int)

    # Realizamos el cambio de nombres de columnas
    victimas.rename(columns={'prov_residencia_persona_en_situacion_violencia': 'provincia',
                                  'genero_persona_en_situacion_de_violencia': 'genero',
                                  'edad_persona_en_situacion_de_violencia': 'edad',
                                  'pais_nacimiento_persona_en_situacion_de_violencia': 'pais',
                                  'tipo_de_violencia_fisica': 'violencia_fisica',
                                  'tipo_de_violencia_psicologica': 'violencia_psicologica',
                                  'tipo_de_violencia_sexual': 'violencia_sexual',
                                  'tipo_de_violencia_economica_y_patrimonial': 'violencia_economica',
                                  'tipo_de_violencia_simbolica': 'violencia_simbolica',
                                  'tipo_de_violencia_domestica': 'violencia_domestica',
                                  'modalidad_de_violencia_institucional': 'violencia_institucional',
                                  'modalidad_de_violencia_laboral': 'violencia_laboral',
                                  'modalidad_violencia_contra_libertad_reproductiva': 'violencia_libertad_reproductiva',
                                  'modalidad_de_violencia_obstetrica': 'violencia_obstetrica',
                                  'modalidad_de_violencia_mediatica': 'violencia_mediatica',
                                  'modalidad_de_violencia_otras': 'violencia_otras',
                                  'vinculo_con_la_persona_agresora': 'vinculo_agresor',
                                  'genero_de_la_persona_agresora': 'genero_agresor'}, inplace=True)

    # Carga el DataFrame en la tabla de la base de datos sin borrar los datos anteriores
    victimas.to_sql(nombre_tabla, engine, index=False, if_exists='append')
    print('Datos cargados correctamente', archivo)

conexion.close()
print("Datos cargados exitosamente en la tabla de la base de datos.")

