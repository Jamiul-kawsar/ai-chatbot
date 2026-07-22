import os

from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

if HF_API_TOKEN is None:
    raise ValueError("Hugging Face API token is missing.")

if MODEL_NAME is None:
    raise ValueError("Model name is missing.")

if REQUEST_TIMEOUT is None:
    raise ValueError("Request timeout is missing.")