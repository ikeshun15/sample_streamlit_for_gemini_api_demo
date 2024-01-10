from typing import Any, List

class GeminiProVisionChatEntity:
    def __init__(self, image_path: str, prompt: str, response: str) -> None:
        self._image_path = image_path
        self._prompt = prompt
        self._response = response
    
    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def response(self) -> str:
        return self._response

    def check_is_same(self, other: Any) -> bool:
        return False