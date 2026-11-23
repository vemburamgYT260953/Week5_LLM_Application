import json
import os
import uuid

MEMORY_DIR = "data/conversations"

def create_conversation_id():
    return str(uuid.uuid4())
def validate_messages(messages):
    if not isinstance(messages, list):
        raise ValueError("Messages must be a list")

    for message in messages:
        if not isinstance(message, dict):
            raise ValueError("Each message must be a dictionary")

        if message.get("role") not in ["user", "assistant"]:
            raise ValueError("Invalid message role")

        if not isinstance(message.get("content"), str):
            raise ValueError("Message content must be a string")

    return True

def save_conversation(conversation_id, messages):
    validate_messages(messages)

    os.makedirs(MEMORY_DIR, exist_ok=True)

    file_path = os.path.join(
        MEMORY_DIR,
        f"{conversation_id}.json"
    )

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4)

def load_conversation(conversation_id):
    file_path = os.path.join(
        MEMORY_DIR,
        f"{conversation_id}.json"
    )

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        messages = json.load(file)

    validate_messages(messages)

    return messages