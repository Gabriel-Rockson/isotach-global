from django.core.files.storage import default_storage as storage
from PIL import Image


def resize_image(image, image_name, width, height):
    size = (width, height)

    image = Image.open(image)
    resized_image = image.resize(size, Image.ANTIALIAS)

    with storage.open(image_name, 'wb') as fh:
        picture_format = 'JPEG'
        resized_image.save(fh, picture_format)
