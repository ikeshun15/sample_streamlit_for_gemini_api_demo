from .base_s_state import BaseSState
from ..entity import GeminiProVisionChatEntity

    
class GeminiProVisionChatSState(BaseSState[GeminiProVisionChatEntity]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_vision_chat"
    
    @staticmethod
    def get_default() -> None:
        return GeminiProVisionChatEntity(image_path="", prompt="", response="")