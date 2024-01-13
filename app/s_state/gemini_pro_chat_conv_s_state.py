from .base_s_state import BaseSState
from typing import List

    
class GeminiProChatConvSState(BaseSState[List]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_chat_conv"
    
    @staticmethod
    def get_default() -> None:
        return []