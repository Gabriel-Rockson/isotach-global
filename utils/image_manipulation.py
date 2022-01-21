from django.core.files.storage import default_storage as storage
from PIL import Image


def resize_image(image, image_name, width, height):
    size = (width, height)

    img = Image.open(image)
    resized_image = img.resize(size, Image.ANTIALIAS)

    with storage.open(image_name, 'wb') as fh:
        picture_format = 'JPEG'
        resized_image.save(fh, picture_format)


# def convert_to_webp(image, image_name):
#     img = Image.open(image)
    
#     with storage.open(image_name, 'wb') as fh:
#         picture_format = 'webp'
#         img.save(fh, picture_format)


def convert_image_to_webp(source):
    destination = source.with_suffix(".webp")
    image = Image.open(source)
    image.save(destination, format="webp")