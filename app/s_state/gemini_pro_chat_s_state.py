from .base_s_state import BaseSState
from ..entity import GeminiProChatEntity

    
class GeminiProChatSState(BaseSState[GeminiProChatEntity]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_chat"
    
    @staticmethod
    def get_default() -> None:
        return GeminiProChatEntity(prompt="", response="")