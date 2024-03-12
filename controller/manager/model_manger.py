import os
from dotenv import load_dotenv
load_dotenv()

from ..handler import GeminiHandler

class ModelManager:
    GeminiHandler.set_api_key(api_key=os.environ['GEMINI_API_KEY'])
    PRO_MODEL = GeminiHandler.set_model(model_name="gemini-1.0-pro-latest")
    PRO_VISION_MODEL = GeminiHandler.set_model(model_name="gemini-pro-vision")
