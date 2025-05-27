#File handling and exception handling

import os

def modify_content(content):
    # Example modification: convert the content to uppercase
    return content.upper()

filename = input("Enter the filename to read: ").strip()

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except IsADirectoryError:
    print(f"Error: '{filename}' is a directory, not a file.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
else:
    modified_content = modify_content(content)
    
    # Generate the new filename
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}_modified{ext}"
    
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Successfully wrote modified content to '{new_filename}'")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{new_filename}'.")
    except FileNotFoundError:
        print(f"Error: The directory path for '{new_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
