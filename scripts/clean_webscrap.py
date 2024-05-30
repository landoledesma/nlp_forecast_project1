import os

def eliminar_archivos_con_signo_porcentaje(directorio):
    # Lista todos los archivos en el directorio dado
    for nombre_archivo in os.listdir(directorio):
        # Comprueba si el nombre del archivo contiene más de un signo "%"
        if nombre_archivo.count('%') > 1:
            ruta_archivo = os.path.join(directorio, nombre_archivo)
            # Elimina el archivo
            os.remove(ruta_archivo)
            print(f'Archivo eliminado: {ruta_archivo}')

if __name__ == "__main__":
    # Especifica el directorio donde se buscarán los archivos
    directorio = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'forecast_data')
    
    eliminar_archivos_con_signo_porcentaje(directorio)
