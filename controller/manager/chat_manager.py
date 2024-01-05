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

    @staticmethod
    def gemini_pro_generate_content(query: str, stream: Optional[bool] = True) -> str:
        if query == "":
            return
        # response = cls.set_model(model_name='gemini-pro').generate_content(contents=query, stream=stream)
        model = GeminiHandler.set_model(model_name='gemini-pro')
        response = GeminiHandler.get_response(model=model, query=query, stream=stream)
        if stream:
            for chunk in response:
                yield chunk.text
        return response.text
    
    @staticmethod
    def gemini_pro_vision_generate_content(image_path: str, query: Optional[str] = None, stream: Optional[bool] = True) -> str:
        if image_path == None:
            return
        img = PillowHandler.open_image(image_path=image_path)
        # response = cls.set_model(model_name='gemini-pro-vision').generate_content(contents=[query, img], stream=stream)
        model = GeminiHandler.set_model(model_name='gemini-pro-vision')
        response = GeminiHandler.get_response_with_image(model=model, query=query, image=img, stream=stream)
        if stream:
            for chunk in response:
                yield chunk.text
        return response.text