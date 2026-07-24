import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

if not OLLAMA_URL:
    raise ValueError("OLLAMA_URL is missing.")

if not OLLAMA_MODEL:
    raise ValueError("OLLAMA_MODEL is missing.")