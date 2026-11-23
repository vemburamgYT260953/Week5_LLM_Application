
import tiktoken


def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)


if __name__ == "__main__":
    prompt = "Explain LLM in simple words"

    total_tokens = count_tokens(prompt)

    print("Prompt:", prompt)
    print("Token Count:", total_tokens)
