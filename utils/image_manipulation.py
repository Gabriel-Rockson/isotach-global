from django.core.files.storage import default_storage as storage
from PIL import Image, ImageEnhance


def resize_image(image, image_name, new_width, new_height=None):
    img = Image.open(image)

    if new_height is None:
        new_height = int((img.height * new_width) / img.width)
        size = new_width, new_height
    else:
        size = new_height, new_height

    resized_image = img.resize(size, Image.ANTIALIAS)

    with storage.open(image_name, 'wb') as fh:
        resized_image.save(fh, format=img.format)

    return resized_image


def reduce_brightness(image, image_name, factor):
    img = Image.open(image)
    enhancer = ImageEnhance.Brightness(img)
    new_img = enhancer.enhance(factor)

    with storage.open(image_name, 'wb') as fh:
        picture_format = 'JPEG'
        new_img.save(fh, picture_format)


def reduce_quality(image, image_name, new_width=None, quality=75):
    img = Image.open(image)

    # Resize the image
    if new_width is None:
        size = img.width, image.height
        resized_image = img.resize(size, Image.ANTIALIAS)
    else:
        resized_image = resize_image(image, image_name, new_width)

    with storage.open(image_name, 'wb') as fh:
        resized_image.save(fh, format=img.format,
                           quality=quality, optimize=True)


def create_thumbnail(image, image_name, new_width, new_height=None, quality=75):
    img = Image.open(image)

    original_image = resize_image(image, image_name, img.width)

    if new_height is None:
        resized_image = resize_image(image, image_name, new_width)
    else:
        resized_image = resize_image(image, image_name, new_width, new_height)

    with storage.open(image.name, 'wb') as fh:
        jpeg_thumbnail = fh.name.split('.')[0] + '.thumbnail.jpg'
        original_image.save(fh, format=img.format)
        resized_image.save(jpeg_thumbnail, format=img.format,
                           quality=quality, optimize=True)
