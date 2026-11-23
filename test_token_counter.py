from app.token_counter import count_tokens, get_token_usage


def test_count_tokens():
    result = count_tokens("Explain LLM")

    assert isinstance(result, int)
    assert result > 0


def test_get_token_usage():
    result = get_token_usage(
        "Explain LLM",
        "LLM is an AI model"
    )

    assert result["prompt_tokens"] > 0
    assert result["response_tokens"] > 0

    assert result["total_tokens"] == (
        result["prompt_tokens"] + result["response_tokens"]
    )