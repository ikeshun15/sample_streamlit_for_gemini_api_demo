from ..handler import GeminiHandler, PillowHandler

import google.generativeai as genai
from typing import Optional
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
    def set_model(model_name: str) -> genai.GenerativeModel:
        return GeminiHandler.set_model(model_name=model_name)

    @classmethod
    def gemini_pro_generate_content(cls, query: str, stream: Optional[bool] = True) -> str:
        return cls.set_model(model_name='gemini-pro').generate_content(contents=query, stream=stream).text
    
    @classmethod
    def gemini_pro_vision_generate_content(cls, image_path: str, query: Optional[str] = None, stream: Optional[bool] = True) -> str:
        img = PillowHandler.open_image(image_path=image_path)
        if query != None:
            return cls.set_model(model_name='gemini-pro-vision').generate_content(contents=[query, img], stream=stream).text
        return cls.set_model(model_name='gemini-pro-vision').generate_content(contents=img, stream=stream).text