from ..handler import GeminiHandler
from model import PillowHandler

import google.generativeai as genai
from typing import Callable, Optional, List
import os
from dotenv import load_dotenv
load_dotenv()

class ChatManager:
    @staticmethod
    def set_default_api_key() -> None:
        GeminiHandler.set_api_key(api_key=os.environ['GEMINI_API_KEY'])

    @staticmethod
    def set_user_api_key(api_key: str) -> None:
        GeminiHandler.set_api_key(api_key=api_key)

    @staticmethod
    def gemini_pro_generate_content(prompt: str, stream: Optional[bool] = True, callback_func: Callable[[str], None] = print) -> str:
        if prompt == "":
            return

        response = GeminiHandler.get_response(model_name="gemini-pro", prompt=prompt, stream=stream)
        if stream:
            answer = ""
            for chunk in response:
                answer += chunk.text
                callback_func(answer)
        return response.text
    
    @staticmethod
    def gemini_pro_chat_content(prompt: str, stream: Optional[bool] = True, history: Optional[List] = [], callback_func: Callable[[str], None] = print) -> tuple[str, List]:
        if prompt == "":
            return
        
        chat_response, chat_history = GeminiHandler.get_chat_response_and_history(model_name="gemini-pro", prompt=prompt, stream=stream, history=history)
        if stream:
            answer = ""
            for chunk in chat_response:
                answer += chunk.text
                callback_func(answer)
        return chat_response.text, chat_history
    
    @staticmethod
    def gemini_pro_vision_generate_content(image_path: str, prompt: Optional[str] = None, stream: Optional[bool] = True, callback_func: Callable[[str], None] = print) -> str:
        if image_path == None:
            return
        img = PillowHandler.open_image(image_path=image_path)

        response = GeminiHandler.get_response_with_image(model_name="gemini-pro-vision", prompt=prompt, image=img, stream=stream)
        if stream:
            answer = ""
            for chunk in response:
                answer += chunk.text
                callback_func(answer)
        return response.text