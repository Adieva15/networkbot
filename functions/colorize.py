import requests
from config import IMAGE_COLORIZATION

def colorize_photo(image_bytes:bytes)->bytes:
    response=requests.post(IMAGE_COLORIZATION, data=image_bytes)
    return response