import google.generativeai as genai
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
    def get_response(model: genai.GenerativeModel, prompt: str, stream: bool):
        return model.generate_content(contents=prompt, stream=stream)
        
    @staticmethod
    def get_response_with_image(model: genai.GenerativeModel, prompt: Optional[str], image: Image.Image, stream: bool):
        return model.generate_content(contents=[prompt, image], stream=stream)
    
    @staticmethod
    def set_chat(model: genai.GenerativeModel, history: Optional[List] = []) -> genai.ChatSession:
        return model.start_chat(history=history)

    # @classmethod
    # def get_chat_response(cls, model_name: str, prompt: str, stream: str, history: Optional[List] = []):
    #     chat = cls.set_chat(model_name=model_name, history=history)
    #     return chat.send_message(content=prompt, stream=stream), chat.history
    
    @staticmethod
    def get_chat_response(chat: genai.ChatSession, prompt: str, stream: str):
        return chat.send_message(content=prompt, stream=stream)
    
    @staticmethod
    def get_chat_history(chat: genai.ChatSession) -> List:
        return chat.history
    
    # @classmethod
    # def get_chat_history(cls, model_name: str, history: Optional[List] = []) -> List:
    #     chat = cls.set_chat(model_name=model_name, history=history)
    #     return chat.history