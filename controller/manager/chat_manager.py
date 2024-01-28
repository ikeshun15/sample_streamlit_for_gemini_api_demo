import google.generativeai as genai
from google.generativeai.types import generation_types
from typing import Callable, Optional, List
import os
from dotenv import load_dotenv
load_dotenv()

from ..handler import GeminiHandler
from .model_manger import ModelManager
from model import PillowHandler

class ChatManager:
    @staticmethod
    def set_gemini_pro_chat(history: Optional[List] = []):
        return GeminiHandler.set_chat(model=ModelManager.PRO_MODEL, history=history)
    
    @staticmethod
    def get_gemini_pro_chat_content(chat: genai.ChatSession, prompt: str, stream: Optional[bool] = True, history: Optional[List] = [], callback_func: Callable[[str], None] = print) -> List:
        if prompt == "":
            return
        
        chat_response = GeminiHandler.get_chat_response(chat=chat, prompt=prompt, stream=stream)
        if stream:
            answer = ""
            for chunk in chat_response:
                answer += chunk.text
                callback_func(answer)
        return chat_response.text
    
    @staticmethod
    def gemini_pro_vision_generate_content(image_path: str, prompt: Optional[str] = None, stream: Optional[bool] = True, callback_func: Callable[[str], None] = print) -> str:
        if image_path == None:
            return
        img = PillowHandler.open_image(image_path=image_path)

        model = GeminiHandler.set_model(model_name="gemini-pro-vision")
        response = GeminiHandler.get_response_with_image(model=model, prompt=prompt, image=img, stream=stream)
        if stream:
            answer = ""
            for chunk in response:
                answer += chunk.text
                callback_func(answer)
        return response.text