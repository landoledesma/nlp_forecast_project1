import os

def delete_files_with_percentage_sign(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename contains more than one "%"
        if filename.count('%') > 1:
            file_path = os.path.join(directory, filename)
            # Delete the file
            os.remove(file_path)
            print(f'File deleted: {file_path}')

if __name__ == "__main__":
    # Specify the directory where the files will be searched
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'forecast_data')
    
    delete_files_with_percentage_sign(directory)
