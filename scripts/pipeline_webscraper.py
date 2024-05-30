import os
import subprocess


def ensure_data_directory_exists():
    data_directory = os.path.join(os.getcwd(), '..', 'data')
    data_directory = os.path.abspath(data_directory)
    
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        print(f"Directory {data_directory} created.")
    else:
        print(f"Directory {data_directory} already exists.")



def build_and_run_docker_container():
    # Starts the Docker container using docker-compose
    subprocess.run(["docker-compose", "up", "--build"])
    print("Docker container started and web scraping script executed.")

def remove_docker_container():
    # Removes the Docker container
    subprocess.run(["docker-compose", "down"])
    print("Docker container removed.")

def clean_files():
    # Executes the clean.py script to remove junk files
    subprocess.run(["python", "scripts/clean_webscrap.py"])
    print("Junk files removed.")

if __name__ == "__main__":
    ensure_data_directory_exists()
    build_and_run_docker_container()
    remove_docker_container()
    clean_files()
