from fastapi import APIRouter

from app.models import ChatRequest, ChatResponse
from app.services.memory import ConversationMemory
from app.services.chat_service import ChatService
from app.services.llm_service import LLMService

router = APIRouter()

memory = ConversationMemory()
llm = LLMService()
chat_service = ChatService(memory, llm)  # Initialize with None for now; will be set in main.py



@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = chat_service.chat(request.message)

    return ChatResponse(reply=reply)


@router.get("/history")
def history():
    return chat_service.get_history()

@router.get("/health")
def health():
    return {"status": "healthy"}