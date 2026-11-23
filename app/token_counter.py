import tiktoken


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """Count tokens using the model's tokenizer."""

    encoding = tiktoken.encoding_for_model(model)

    return len(encoding.encode(text))


def get_token_usage(prompt: str, response: str) -> dict:
    """Calculate prompt, response and total token usage."""

    prompt_tokens = count_tokens(prompt)
    response_tokens = count_tokens(response)

    return {
        "prompt_tokens": prompt_tokens,
        "response_tokens": response_tokens,
        "total_tokens": prompt_tokens + response_tokens
    }