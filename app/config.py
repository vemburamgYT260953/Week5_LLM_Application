
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4o-mini"
    )

    ANTHROPIC_MODEL = os.getenv(
        "ANTHROPIC_MODEL",
        "claude-3-5-haiku-latest"
    )

    API_KEY = os.getenv("API_KEY")

settings = Settings()
