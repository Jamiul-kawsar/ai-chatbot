from huggingface_hub import InferenceClient
from app.config import HF_API_TOKEN, MODEL_NAME, REQUEST_TIMEOUT
from httpx import ConnectError, TimeoutException
from fastapi import HTTPException

class LLMService:
    def __init__(self):
        self.client = InferenceClient(
            provider="auto",
            api_key=HF_API_TOKEN,
            timeout=REQUEST_TIMEOUT,
        )

        self.model = MODEL_NAME

    
    def generate_response(self, messages):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=512,
                )
                return response.choices[0].message.content
            except ConnectError:
                raise HTTPException(
                status_code=503,
                detail="No internet connection. Please check your network and try again."
            )
            except TimeoutException:
                raise HTTPException(
                    status_code=504,
                    detail="The AI service timed out. Please try again later."
                )

            except Exception:
                raise HTTPException(
                    status_code=500,
                    detail="An unexpected error occurred."
                )
    