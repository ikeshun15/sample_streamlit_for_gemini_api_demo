import PIL.Image

class PillowHandler:
    @staticmethod
    def open_image(image_path: str) -> PIL.Image:
        return PIL.Image.open(fp=image_path)