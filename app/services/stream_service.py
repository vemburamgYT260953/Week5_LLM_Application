
import time

from app.services.mock_llm import stream_openai


def generate_stream(prompt: str, messages: list = None):
    """Generate mock LLM response using conversation history."""

    start_time = time.perf_counter()
    first_token_time = None

    try:
        conversation = messages or []

        full_prompt = ""

        for message in conversation:
            role = message.get("role", "user")
            content = message.get("content", "")

            full_prompt += f"{role}: {content}\n"

        full_prompt += f"user: {prompt}"

        for chunk in stream_openai(full_prompt):

            if first_token_time is None:
                first_token_time = time.perf_counter() - start_time
                print(
                    f"\nFirst token time: {first_token_time:.4f} seconds"
                )

            yield chunk

    except Exception as e:
        print(f"Streaming error: {type(e).__name__}: {e}")
        yield "An error occurred while generating the response."
