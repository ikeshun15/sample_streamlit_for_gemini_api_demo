import google.generativeai as genai
from google.ai import generativelanguage as glm
from typing import List

from controller import ChatManager

class GeminiProChatEntity:
    def __init__(self) -> None:
        self._chat = ChatManager.set_gemini_pro_chat()

    @property
    def chat(self) -> str:
        return self._chat

    def get_chat_history_list(self) -> List[glm.Content]:
        chat_history_list = []
        for message in self._chat.history:
            chat_history_list.append(message)
        return chat_history_list