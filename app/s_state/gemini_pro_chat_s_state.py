import streamlit as st

from .base_s_state import BaseSState
from ..entity import GeminiProChatEntity

    
class GeminiProChatSState(BaseSState[GeminiProChatEntity]):
    @staticmethod
    def get_name() -> str:
        return "gemini_pro_chat"
    
    @staticmethod
    def get_default() -> None:
        return GeminiProChatEntity(user_message=st.empty(), gemini_message=st.empty(), prompt=None, response=None)