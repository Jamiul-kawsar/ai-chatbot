from fastapi import FastAPI

from app.routes.chat import router as chat_router

app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0",
    description="Simple AI Chatbot"
)

app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AI Chatbot API is running."
    }