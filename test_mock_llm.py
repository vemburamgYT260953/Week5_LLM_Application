
from app.services.mock_llm import (
    ask_openai,
    ask_claude,
    stream_openai
)


def test_openai_mock():
    result = ask_openai("Explain what an LLM is.")

    assert isinstance(result, dict)
    assert "answer" in result
    assert len(result["answer"]) > 0


def test_claude_mock():
    result = ask_claude(
        "What is Python?",
        "You are a helpful AI assistant."
    )

    assert isinstance(result, dict)
    assert "answer" in result
    assert len(result["answer"]) > 0


def test_openai_stream():
    chunks = list(stream_openai("Explain LLM"))

    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)

    response = "".join(chunks)
    assert len(response) > 0
