import pytest
from unittest.mock import AsyncMock, MagicMock

from app.services.llm_service import (
    async_ask_openai,
    async_ask_claude
)


@pytest.mark.asyncio
async def test_async_openai():

    mock_response = MagicMock()
    mock_response.model = "gpt-4o-mini"

    mock_response.choices = [
        MagicMock(
            message=MagicMock(content="Test OpenAI response")
        )
    ]

    mock_response.usage.prompt_tokens = 5
    mock_response.usage.completion_tokens = 10
    mock_response.usage.total_tokens = 15

    from app.services import llm_service

    llm_service.async_openai_client.chat.completions.create = AsyncMock(
        return_value=mock_response
    )

    result = await async_ask_openai("Explain LLM")

    assert result["provider"] == "OpenAI"
    assert result["answer"] == "Test OpenAI response"
    assert result["total_tokens"] == 15


@pytest.mark.asyncio
async def test_async_claude():

    mock_response = MagicMock()
    mock_response.model = "claude-test"

    mock_response.content = [
        MagicMock(
            type="text",
            text="Test Claude response"
        )
    ]

    mock_response.usage.input_tokens = 5
    mock_response.usage.output_tokens = 10

    from app.services import llm_service

    llm_service.async_claude_client.messages.create = AsyncMock(
        return_value=mock_response
    )

    result = await async_ask_claude(
        "Explain Python",
        "You are a helpful assistant."
    )

    assert result["provider"] == "Anthropic"
    assert result["answer"] == "Test Claude response"
    assert result["total_tokens"] == 15