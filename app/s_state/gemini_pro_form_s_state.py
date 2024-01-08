from .base_s_state import BaseSState

    
class GeminiProFormSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_form_state"
    
    @staticmethod
    def get_default() -> bool:
        return False