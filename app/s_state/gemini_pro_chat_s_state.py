from .base_s_state import BaseSState
from ..entity import GeminiProChatEntity
from typing import List

    
class GeminiProChatSState(BaseSState[GeminiProChatEntity]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_chat_conv"
    
    @staticmethod
    def get_default() -> None:
        return GeminiProChatEntity()