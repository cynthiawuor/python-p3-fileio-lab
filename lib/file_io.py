# lib/file_io.py

def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"
    
    try:
        with open(file_name, "w") as file:
            file.write(file_content)
    except IOError as e:
        print(f"Error writing to {file_name}: {e}")

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"
    
    try:
        with open(file_name, "a") as file:
            if not append_content.endswith("\n"):
                append_content += "\n"  
            file.write(append_content)
    except IOError as e:
        print(f"Error appending to {file_name}: {e}")

def read_file(file_name):
    file_name = str(file_name) + ".txt"
    
    try:
        with open(file_name, "r") as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error reading from {file_name}: {e}")
        return None
