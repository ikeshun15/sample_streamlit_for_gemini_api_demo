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

    @classmethod
    def get_response(cls, model_name: str, prompt: str, stream: bool) -> str:
        model = cls.set_model(model_name=model_name)
        return model.generate_content(contents=prompt, stream=stream)
        
    @classmethod
    def get_response_with_image(cls, model_name: str, prompt: Optional[str], image: Image.Image, stream: bool) -> str:
        model = cls.set_model(model_name=model_name)
        return model.generate_content(contents=[prompt, image], stream=stream)
    
    @classmethod
    def get_chat_response_and_history(cls, model_name: str, prompt: str, stream: str, history: Optional[List] = []) -> tuple[str, List]:
        model = cls.set_model(model_name=model_name)
        chat = model.start_chat(history=history)
        return chat.send_message(content=prompt, stream=stream), chat.history
    
    # @classmethod
    # def get_chat_response_and_history(cls, model_name: str, prompt: str, stream: str, chat: Optional[genai.ChatSession] = None) -> str:
    #     model = cls.set_model(model_name=model_name)
    #     if chat == None:
    #         chat = model.start_chat(history=[])
    #     return chat.send_message(content=prompt, stream=stream), chat.history