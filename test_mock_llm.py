
from app.services.mock_llm import (
    ask_openai,
    ask_claude,
    stream_openai
)

if __name__ == "__main__":

    print("========== OPENAI MOCK ==========")

    result = ask_openai(
        "Explain what an LLM is."
    )

    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n========== CLAUDE MOCK ==========")

    claude_result = ask_claude(
        "What is Python?",
        "You are a helpful AI assistant."
    )

    for key, value in claude_result.items():
        print(f"{key}: {value}")

    print("\n========== STREAMING MOCK ==========")

    for chunk in stream_openai("Explain LLM"):
        print(chunk, end="", flush=True)

    print("\n\nMock testing completed!")
