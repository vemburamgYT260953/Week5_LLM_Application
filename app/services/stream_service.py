
import time

from app.services.mock_llm import stream_openai


def generate_stream(prompt: str):
    """Generate mock LLM response with safe error handling."""

    start_time = time.perf_counter()
    first_token_time = None

    try:
        for chunk in stream_openai(prompt):

            if first_token_time is None:
                first_token_time = time.perf_counter() - start_time
                print(
                    f"\nFirst token time: {first_token_time:.4f} seconds"
                )

            yield chunk

    except Exception as e:
        print(f"Streaming error: {type(e).__name__}: {e}")
        yield "An error occurred while generating the response."
