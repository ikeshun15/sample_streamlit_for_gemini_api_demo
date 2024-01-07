from ..handler import PillowHandler

class ImageManager:
    @staticmethod
    def display_input_image(image_path: str) -> str:
        return PillowHandler.open_image(image_path=image_path)