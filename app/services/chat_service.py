from app.logger import logger

from app.services.memory import ConversationMemory
from app.services.llm_service import LLMService


class ChatService:
    def __init__(self, memory: ConversationMemory, llm: LLMService):
        self.memory = memory
        self.llm = llm

    def chat(self, user_message: str) -> str:
        # Save user's message
        self.memory.add_message("user", user_message)

        # Temporary reply until LLM is connected
        ai_reply = self.llm.generate_response(
            self.memory.get_messages()
        )

        # Save assistant's reply
        self.memory.add_message("assistant", ai_reply)

        return ai_reply

    def get_history(self) -> list:
        logger.info("Getting conversation history...")
        messages = self.memory.get_messages()
        logger.info("Conversation history: %s", messages)
        return messages

    def clear_history(self) -> None:
        self.memory.clear()