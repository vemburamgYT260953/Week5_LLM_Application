
from openai import OpenAI
from anthropic import Anthropic

from app.config import settings


# Initialize clients
openai_client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

claude_client = Anthropic(
    api_key=settings.ANTHROPIC_API_KEY
)


def ask_openai(prompt: str):
    """Send a prompt to OpenAI and return answer and usage."""

    response = openai_client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    return {
        "provider": "OpenAI",
        "model": response.model,
        "answer": answer,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens
    }


def ask_claude(prompt: str, system: str):
    """Send a prompt to Claude and return answer and usage."""

    response = claude_client.messages.create(
        model=settings.ANTHROPIC_MODEL,
        max_tokens=500,
        system=system,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = "".join(
        block.text
        for block in response.content
        if block.type == "text"
    )

    return {
        "provider": "Anthropic",
        "model": response.model,
        "answer": answer,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "total_tokens": (
            response.usage.input_tokens
            + response.usage.output_tokens
        )
    }
