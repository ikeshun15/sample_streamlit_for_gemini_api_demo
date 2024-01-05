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

    @staticmethod
    def get_response(model: genai.GenerativeModel, query: str, stream: bool) -> str:
        return model.generate_content(contents=query, stream=stream)
        
    @staticmethod
    def get_response_with_image(model: genai.GenerativeModel, query: Optional[str], image: Image.Image, stream: bool) -> str:
        return model.generate_content(contents=[query, image], stream=stream)