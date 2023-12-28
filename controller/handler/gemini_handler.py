import google.generativeai as genai

class GeminiHandler:
    @staticmethod
    def set_api_key(api_key: str) -> None:
        genai.configure(api_key=api_key)

    @staticmethod
    def set_model(model_name: str) -> genai.GenerativeModel:
        return genai.GenerativeModel(model_name=model_name)
    
    # @classmethod
    # def generate_chunk(cls, model_name: str, query: str, stream: bool) -> str:
    #     response = cls.set_model(model_name).generate_content(contents=query, stream=stream)
    #     if stream:
    #         for chunk in response:
    #             yield chunk.text
    #     yield response.text
