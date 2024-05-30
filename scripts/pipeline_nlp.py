import zipfile
import os
import shutil
from csv_nlp import parse_xml
import pandas as pd

def unzip_file(zip_path, extract_to):
    # Check if the destination folder exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
        print(f"Directory created: {extract_to}")
    else:
        # If the folder exists, check if it is empty
        if os.listdir(extract_to):
            print(f"Files found in {extract_to}. They will be deleted and new files will be added.")
            shutil.rmtree(extract_to)
            os.makedirs(extract_to)
    
    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Files unzipped to: {extract_to}")

if __name__ == "__main__":
    # Path to the zip file (adjust the path according to your folder structure)
    zip_path = "2020.zip"
    extract_to = "data/nlp_data"
    
    # Ensure the zip file exists
    if not os.path.isfile(zip_path):
        print(f"The file {zip_path} was not found")
    else:
        unzip_file(zip_path, extract_to)

    # Get the base path of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define relative paths based on the base path
    xml_folder_path = os.path.join(current_directory, '..', 'data', 'nlp_data')
    csv_folder_path = os.path.join(current_directory, '..', 'data', 'source')
    # List to store all data rows
    all_data = []

    # Iterate over all XML files in the folder
    for filename in os.listdir(xml_folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(xml_folder_path, filename)
            all_data.extend(parse_xml(file_path))

    # Create a DataFrame with all the data
    df = pd.DataFrame(all_data)

    # Create the folder to save the CSV file if it doesn't exist
    os.makedirs(csv_folder_path, exist_ok=True)
    csv_file_path = os.path.join(csv_folder_path, 'abstract.csv')
    
    # Save the DataFrame as a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f'CSV file saved to {csv_file_path}')
