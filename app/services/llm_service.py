import httpx
from fastapi import HTTPException
from httpx import ConnectError, TimeoutException

from app.config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
    REQUEST_TIMEOUT,
)
from app.logger import logger


class LLMService:
    def generate_response(self, messages: list[dict]) -> str:
        try:
            response = httpx.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "messages": messages,
                    "stream": False,
                },
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            data = response.json()

            return data["message"]["content"]

        except ConnectError:
            raise HTTPException(
                status_code=503,
                detail="Cannot connect to Ollama. Is the Ollama server running?",
            )

        except TimeoutException:
            raise HTTPException(
                status_code=504,
                detail="The AI model timed out.",
            )

        except httpx.HTTPStatusError as e:
            logger.exception("Ollama API error")
            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text,
            )

        except Exception:
            logger.exception("Unexpected error")
            raise HTTPException(
                status_code=500,
                detail="Internal server error.",
            )