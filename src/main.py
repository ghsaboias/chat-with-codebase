import os
from src.conversation_history import ConversationHistory
from src.claude_chat import ClaudeChat

def read_codebase_content():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(script_dir, 'data', 'output.txt')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file 'output.txt' was not found in {os.path.dirname(file_path)}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None

def main():
    codebase_content = read_codebase_content()
    if codebase_content is None:
        print("Exiting due to file read error.")
        exit(1)

    print(f"Read {len(codebase_content)} characters from the codebase.")

    conversation_history = ConversationHistory()
    claude_chat = ClaudeChat()

    system_message = f"<file_contents>{codebase_content}</file_contents>"

    print("Starting conversation with Claude. Type 'exit' to end the conversation.")
    while True:
        user_input = input("\nYour message: ")
        if user_input.lower() == 'exit':
            break
        
        assistant_reply = claude_chat.send_message(system_message, conversation_history, user_input)
        
        conversation_history.add_turn("user", user_input)
        conversation_history.add_turn("assistant", assistant_reply)

if __name__ == "__main__":
    main()