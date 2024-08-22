# write_directory_contents.py

import os

def write_directory_contents_to_file(directory_path, output_file_path):
    # Files and directories to ignore
    ignore_list = {'venv', '.gitignore', 'package-lock.json', 'eslint.config.js', 'node_modules', '.git', 'DS_Store'}
    
    print(f"Starting to process directory: {directory_path}")
    print(f"Output will be written to: {output_file_path}")
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(directory_path):
            print(f"Current directory: {root}")
            
            # Remove ignored directories from dirs to prevent them from being searched
            dirs[:] = [d for d in dirs if d not in ignore_list]
            print(f"Subdirectories (after ignoring): {dirs}")
            
            print(f"Files: {files}")
            
            for file in files:
                if file not in ignore_list:
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
                    print(f"Ignored file: {file}")

    print("Finished processing all files")

if __name__ == "__main__":
    directory_path = os.path.expanduser('~/Documents/chat-app')
    output_file_path = 'output.txt'
    write_directory_contents_to_file(directory_path, output_file_path)
    
    print(f"Check if output file exists: {os.path.exists(output_file_path)}")
    if os.path.exists(output_file_path):
        print(f"Output file size: {os.path.getsize(output_file_path)} bytes")