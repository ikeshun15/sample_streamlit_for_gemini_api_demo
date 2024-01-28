import google.generativeai as genai
from google.generativeai.types import generation_types
from typing import Any, List

from controller import ChatManager

class GeminiProChatEntity:
    def __init__(self) -> None:
        self._chat = ChatManager.set_gemini_pro_chat()

    @property
    def chat(self) -> str:
        return self._chat
    
    @property
    def chat_history(self) -> str:
        return self._chat.history

    def get_chat_history_list(self):
        chat_history_list = []
        for message in self._chat.history:
            chat_history_list.append(message)
        return chat_history_list
    
    def get_role_list(self):
        role_list = []
        for message in self._chat.history:
            role_list.append(message.role)
        return role_list
    
    def get_message_list(self):
        message_list = []
        for message in self._chat.history:
            message_list.append(message.parts[0])
        return message_list