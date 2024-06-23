import google.generativeai as genai
from google.generativeai.types import generation_types
from PIL import Image
from typing import Optional, List

class GeminiHandler:
    @staticmethod
    def set_api_key(api_key: str) -> None:
        genai.configure(api_key=api_key)

    @staticmethod
    def set_model(model_name: str) -> genai.GenerativeModel:
        return genai.GenerativeModel(model_name=model_name)
        
    @staticmethod
    def get_response_with_image(model: genai.GenerativeModel, prompt: Optional[str], image: Image.Image, stream: bool) -> generation_types.GenerateContentResponse:
        return model.generate_content(contents=[prompt, image], stream=stream)
    
    @staticmethod
    def set_chat(model: genai.GenerativeModel, history: Optional[List] = []) -> genai.ChatSession:
        return model.start_chat(history=history)
    
    @staticmethod
    def get_chat_response(chat: genai.ChatSession, prompt: str, stream: str) -> generation_types.GenerateContentResponse:
        return chat.send_message(content=prompt, stream=stream)