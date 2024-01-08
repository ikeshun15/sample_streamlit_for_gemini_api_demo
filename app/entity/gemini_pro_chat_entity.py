from typing import Any, List
from streamlit.delta_generator import DeltaGenerator

class GeminiProChatEntity:
    def __init__(self, user_message: DeltaGenerator, gemini_message: DeltaGenerator, prompt:str, response: str) -> None:
        self._user_message = user_message
        self._gemini_message = gemini_message
        self._prompt = prompt
        self._response = response

    @property
    def user_message(self) -> DeltaGenerator:
        return self._user_message

    @property
    def gemini_message(self) -> DeltaGenerator:
        return self._gemini_message
    
    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def response(self) -> str:
        return self._response

    def check_is_same(self, other: Any) -> bool:
        return False