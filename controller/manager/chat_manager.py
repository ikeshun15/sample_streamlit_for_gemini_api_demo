import google.generativeai as genai
from typing import Callable, Optional, List
from dotenv import load_dotenv
load_dotenv()

from ..handler import GeminiHandler
from .model_manger import ModelManager
from model import PillowHandler

class ChatManager:
    @staticmethod
    def set_gemini_pro_chat(history: Optional[List] = []):
        return GeminiHandler.set_chat(model=ModelManager.PRO_MODEL, history=history)

    def get_gemini_pro_chat_generator(chat: genai.ChatSession, prompt: str, stream: Optional[bool] = True):
        if prompt == "":
            return

        chat_response = GeminiHandler.get_chat_response(chat=chat, prompt=prompt, stream=stream)
        if stream:
            for chunk in chat_response:
                # レスポンスの各部分のテキストを取得
                parts_text = [part.text for part in chunk.parts]

                # テキスト部分を結合して最終的なレスポンスを作成
                final_response = " ".join(parts_text)

                yield final_response

    
    @staticmethod
    def gemini_pro_vision_generate_content(image_path: str, prompt: Optional[str] = None, stream: Optional[bool] = True, callback_func: Callable[[str], None] = print) -> str:
        if image_path == None:
            return
        img = PillowHandler.open_image(image_path=image_path)

        response = GeminiHandler.get_response_with_image(model=ModelManager.PRO_VISION_MODEL, prompt=prompt, image=img, stream=stream)
        if stream:
            answer = ""
            for chunk in response:
                answer += chunk.text
                callback_func(answer)
        return response.text