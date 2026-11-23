from app.services.llm_service import ask_openai


if __name__ == "__main__":
    result = ask_openai(
        "Explain what an LLM is in two sentences."
    )

    print("\nProvider:", result["provider"])
    print("Model:", result["model"])
    print("Answer:", result["answer"])
    print("Input tokens:", result["input_tokens"])
    print("Output tokens:", result["output_tokens"])
    print("Total tokens:", result["total_tokens"])