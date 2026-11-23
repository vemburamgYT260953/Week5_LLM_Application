
def ask_openai(prompt: str):
    """Mock OpenAI response for local development."""

    answer = (
        "An LLM (Large Language Model) is an AI model "
        "trained on large amounts of text. "
        "It understands prompts and generates human-like responses."
    )

    input_tokens = len(prompt.split())
    output_tokens = len(answer.split())

    return {
        "provider": "OpenAI (Mock)",
        "model": "mock-gpt-4o-mini",
        "answer": answer,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens
    }


def ask_claude(prompt: str, system: str):
    """Mock Claude response for local development."""

    answer = (
        "Claude is an AI assistant developed by Anthropic. "
        "It can understand instructions and generate useful responses."
    )

    input_tokens = len((system + " " + prompt).split())
    output_tokens = len(answer.split())

    return {
        "provider": "Anthropic (Mock)",
        "model": "mock-claude",
        "answer": answer,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens
    }



# def stream_openai(prompt: str):
#     """Generate a mock streaming response with controlled failure."""

#     if prompt == "TEST_ERROR":
#         yield "Starting test... "
#         raise RuntimeError("Simulated streaming failure")

#     answer = ask_openai(prompt)["answer"]

#     for word in answer.split():
#         yield word + " "



def stream_openai(prompt: str):
    """Generate a mock streaming response."""

    answer = ask_openai(prompt)["answer"]

    for word in answer.split():
        yield word + " "
