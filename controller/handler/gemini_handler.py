import google.generativeai as genai
from PIL import Image
from typing import Optional

class GeminiHandler:
    @staticmethod
    def set_api_key(api_key: str) -> None:
        genai.configure(api_key=api_key)

    @staticmethod
    def set_model(model_name: str) -> genai.GenerativeModel:
        return genai.GenerativeModel(model_name=model_name)

    @classmethod
    def get_response(cls, model_name: str, query: str, stream: bool) -> str:
        model = cls.set_model(model_name=model_name)
        return model.generate_content(contents=query, stream=stream)
        
    @classmethod
    def get_response_with_image(cls, model_name: str, query: Optional[str], image: Image.Image, stream: bool) -> str:
        model = cls.set_model(model_name=model_name)
        return model.generate_content(contents=[query, image], stream=stream)