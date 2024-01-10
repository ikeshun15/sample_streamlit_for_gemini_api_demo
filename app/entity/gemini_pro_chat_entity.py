from typing import Any, List

class GeminiProChatEntity:
    def __init__(self, prompt: str, response: str) -> None:
        self._prompt = prompt
        self._response = response
    
    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def response(self) -> str:
        return self._response

    def check_is_same(self, other: Any) -> bool:
        return False