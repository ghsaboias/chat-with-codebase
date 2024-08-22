class ConversationHistory:
    def __init__(self):
        self.turns = []

    def add_turn(self, role, content):
        self.turns.append({
            "role": role,
            "content": [
                {
                    "type": "text",
                    "text": content
                }
            ]
        })

    def get_turns(self):
        result = []
        user_turns_processed = 0
        for turn in reversed(self.turns):
            if turn["role"] == "user" and user_turns_processed < 2:
                result.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": turn["content"][0]["text"],
                            "cache_control": {"type": "ephemeral"}
                        }
                    ]
                })
                user_turns_processed += 1
            else:
                result.append(turn)
        return list(reversed(result))