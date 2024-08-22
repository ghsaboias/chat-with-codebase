import anthropic
import time
import os

client = anthropic.Anthropic()
MODEL_NAME = "claude-3-5-sonnet-20240620"

def read_codebase_content():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'output.txt')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file 'output.txt' was not found in {script_dir}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None

def send_message_to_claude(codebase_content, user_message):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "<codebase>" + codebase_content + "</codebase>",
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": user_message
                }
            ]
        }
    ]

    start_time = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1000,
        messages=messages,
        extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
    )
    end_time = time.time()

    print(f"\nAPI call time: {end_time - start_time:.2f} seconds")
    print(f"Input tokens: {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print("\nClaude's response:")
    print(response.content[0].text)

    return response

def main():
    # Read the content of the codebase from output.txt
    codebase_content = read_codebase_content()

    if codebase_content is None:
        print("Exiting due to file read error.")
        exit(1)

    print(f"Read {len(codebase_content)} characters from the codebase.")

    # Start conversation
    print("Starting conversation with Claude. Type 'exit' to end the conversation.")
    while True:
        user_input = input("\nYour message: ")
        if user_input.lower() == 'exit':
            break
        
        send_message_to_claude(codebase_content, user_input)

if __name__ == "__main__":
    main()