import os
import sys

def write_directory_contents_to_file(directory_path, output_file_path, file_list):
    # Files and directories to ignore
    ignore_list = {'__pycache__', '.venv', '.gitignore', 'package-lock.json', 'eslint.config.js', 'node_modules', '.git', 'DS_Store'}
    
    print(f"Starting to process directory: {directory_path}")
    print(f"Output will be written to: {output_file_path}")
    print(f"Files to process: {file_list}")
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(directory_path):
            print(f"Current directory: {root}")
            
            # Remove ignored directories from dirs to prevent them from being searched
            dirs[:] = [d for d in dirs if d not in ignore_list]
            print(f"Subdirectories (after ignoring): {dirs}")
            
            for file in files:
                if file in file_list and file not in ignore_list:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory_path)
                    
                    print(f"Processing file: {relative_path}")
                    
                    # Write the file path as a comment
                    output_file.write(f"# {relative_path}\n")
                    
                    # Read and write the contents of the file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as input_file:
                            content = input_file.read()
                            output_file.write(content)
                            print(f"Successfully wrote contents of {relative_path}")
                    except UnicodeDecodeError:
                        output_file.write("# Binary file, contents not shown\n")
                        print(f"Skipped binary file: {relative_path}")
                    except Exception as e:
                        print(f"Error processing {relative_path}: {str(e)}")
                    
                    # Add a newline for separation
                    output_file.write('\n\n')
                else:
                    print(f"Skipped file: {file}")

    print("Finished processing all specified files")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path> <file1> <file2> ...")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_list = sys.argv[2:]

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        exit(1)

    # Create 'data' directory if it doesn't exist
    data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Use a default output file name
    output_file_name = 'output.txt'
    output_file_path = os.path.join(data_dir, output_file_name)

    write_directory_contents_to_file(directory_path, output_file_path, file_list)

    print(f"Check if output file exists: {os.path.exists(output_file_path)}")
    if os.path.exists(output_file_path):
        print(f"Output file size: {os.path.getsize(output_file_path)} bytes")