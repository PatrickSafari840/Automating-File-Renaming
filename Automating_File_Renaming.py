import os

def rename_files(directory_path, prefix):
    # Get list of files in the directory
    files = os.listdir(directory_path)
    
    # Loop through each file
    for file in files:
        # Create the new filename by adding the prefix
        new_name = prefix + file
        
        # Get the full paths of the original and new files
        original_path = os.path.join(directory_path, file)
        new_path = os.path.join(directory_path, new_name)
        
        # Rename the file
        os.rename(original_path, new_path)
        
        print(f'Renamed "{file}" to "{new_name}"')

# Example usage
if __name__ == "__main__":
    directory_path = "/path/to/your/directory"  # Replace this with your directory path
    prefix = "2024_"  # Change this prefix as needed
    
    rename_files(directory_path, prefix)
