import zipfile
import os
import shutil
from csv_nlp import parse_xml
import pandas as pd

def unzip_file(zip_path, extract_to):
    # Verifica si la carpeta de destino existe
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
        print(f"Directorio creado: {extract_to}")
    else:
        # Si la carpeta existe, verifica si está vacía
        if os.listdir(extract_to):
            print(f"Se encontraron archivos en {extract_to}. Se eliminarán y se ingresarán los nuevos archivos.")
            shutil.rmtree(extract_to)
            os.makedirs(extract_to)
    
    # Descomprime el archivo
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Archivos descomprimidos en: {extract_to}")

if __name__ == "__main__":
    # Ruta al archivo zip (ajusta la ruta según tu estructura de carpetas)
    zip_path = "2020.zip"  
    extract_to = "data/nlp_data"
    
    # Asegura que el archivo zip existe
    if not os.path.isfile(zip_path):
        print(f"No se encontró el archivo {zip_path}")
    else:
        unzip_file(zip_path, extract_to)

    # Obtener la ruta base del script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Definir las rutas relativas basadas en la ruta base
    xml_folder_path = os.path.join(current_directory, '..', 'data', 'nlp_data')
    csv_folder_path = os.path.join(current_directory, '..', 'data', 'source')
    # Lista para almacenar todas las filas de datos
    all_data = []

    # Iterar sobre todos los archivos XML en la carpeta
    for filename in os.listdir(xml_folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(xml_folder_path, filename)
            all_data.extend(parse_xml(file_path))

    # Crear un DataFrame con todos los datos
    df = pd.DataFrame(all_data)

    # Crear la carpeta para guardar el archivo CSV si no existe
    os.makedirs(csv_folder_path, exist_ok=True)
    csv_file_path = os.path.join(csv_folder_path, 'abstract.csv')
    
    # Guardar el DataFrame como un archivo CSV
    df.to_csv(csv_file_path, index=False)

    print(f'Archivo CSV guardado en {csv_file_path}')

