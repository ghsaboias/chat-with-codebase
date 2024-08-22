import time
import anthropic
from config import MODEL_NAME

class ClaudeChat:
    def __init__(self):
        self.client = anthropic.Anthropic()

    def send_message(self, system_message, conversation_history, user_message):
        messages = conversation_history.get_turns()
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_message
                }
            ]
        })

        start_time = time.time()
        response = self.client.messages.create(
            model=MODEL_NAME,
            max_tokens=1000,
            system=[
                {"type": "text", "text": system_message, "cache_control": {"type": "ephemeral"}},
            ],
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )
        end_time = time.time()

        print(f"\nAPI call time: {end_time - start_time:.2f} seconds")
        print(f"Input tokens: {response.usage.input_tokens}")
        print(f"Output tokens: {response.usage.output_tokens}")
        print(f"Input tokens (cache read): {getattr(response.usage, 'cache_read_input_tokens', '---')}")
        print(f"Input tokens (cache write): {getattr(response.usage, 'cache_creation_input_tokens', '---')}")

        assistant_reply = response.content[0].text
        print("\nClaude's response:")
        print(assistant_reply)

        return assistant_reply