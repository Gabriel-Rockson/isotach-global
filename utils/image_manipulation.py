from PIL import Image
from django.core.files.storage import default_storage as storage
from PIL import Image, ImageEnhance

from io import BytesIO, StringIO


def resize_image(image, image_name, new_width, new_height=None):
    img = Image.open(image)

    if new_height is None:
        new_height = int((img.height * new_width) / img.width)
        size = new_width, new_height
    else:
        size = new_height, new_height

    resized_image = img.resize(size, Image.ANTIALIAS)

    return resized_image


def reduce_brightness(image, image_name, factor):
    img = Image.open(image)
    enhancer = ImageEnhance.Brightness(img)
    new_img = enhancer.enhance(factor)

    return new_img


def reduce_quality(image, image_name, new_width=None, quality=75):
    img = Image.open(image)

    # Resize the image
    if new_width is None:
        resized_image = resize_image(image, image_name, img.width, img.height)
    else:
        resized_image = resize_image(image, image_name, new_width)

    bfile = BytesIO()
    resized_image.save(bfile, format=img.format,
                       quality=quality, optimize=True)
    with storage.open(image_name, 'wb') as f:
        f.write(bfile.getvalue())


def reduce_brightness_and_quality(image, image_name, factor, new_width=None, quality=75):
    # resize the image
    resized_image = resize_image(image, image_name, new_width=new_width)
    # reduce the brightness
    reduced_brightness_image = reduce_brightness(
        resized_image, image_name, factor=0.3)
    # reduce the quality
    reduce_quality(reduced_brightness_image, image_name,
                   new_width=new_width, quality=65)


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
