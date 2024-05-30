import os
import subprocess
import time

def build_and_run_docker_container():
    # Levanta el contenedor Docker usando docker-compose
    subprocess.run(["docker-compose", "up", "--build"])
    print("Contenedor Docker levantado y script de web scraping ejecutado.")


def remove_docker_container():
    # Elimina el contenedor Docker
    subprocess.run(["docker-compose", "down"])
    print("Contenedor Docker eliminado.")

def clean_files():
    # Ejecuta el script clean.py para eliminar archivos basura
    subprocess.run(["python", "scripts/clean_webscrap.py"])
    print("Archivos basura eliminados.")

if __name__ == "__main__":
    
    build_and_run_docker_container()
    remove_docker_container()
    clean_files()
    
