import requests
import os
from urllib.parse import urlparse, urljoin
from PIL import Image as PILImage

class Image():
    def __init__(self, description: str, image_path: str):
        self.description = description
        self.image_path = image_path


class Message():
    def __init__(self, message: dict):
        self.message = message

    def user_name(self) -> str:
        return self.message['u']['name']
    
    def msg(self) -> str:
        return self.message.get('msg')
    
    def images(self, base_url: str, size: float) -> Image:
        attachments = self.message.get('attachments')
        if attachments is None:
            return None

        images = []

        for i, attachment in enumerate(attachments):
            image_url = attachment.get('image_url')
            if image_url is None:
                return None
            
            path = urlparse(image_url).path
            filename = './downloads/' + os.path.basename(path)

            with open(filename, 'wb') as file:
                img = requests.get(urljoin(base_url, image_url))
                file.write(img.content)

            if size is not None:
                resized_image = PILImage.open(filename)
                resized_image.thumbnail((size, size), resample=PILImage.LANCZOS)
                resized_image.save(filename, quality=95)

            images.append(Image(attachment.get('description'), filename))

        return images
