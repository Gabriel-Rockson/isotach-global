from io import BytesIO

from django.core.files.storage import default_storage as storage
from PIL import Image, ImageEnhance

from time import time


# resize image
def resize_image(image_name, width, height=None, quality=85, format="JPEG"):
    with storage.open(image_name, 'rb') as m:
        im = Image.open(m)

        if height is None:
            height = int((im.height * width) / im.width)
            size = width, height
        else:
            size = width, height

        im = im.resize(size, Image.ANTIALIAS)

        bfile = BytesIO()
        im.save(bfile, format=format, quality=quality)

    with storage.open(image_name, 'wb') as i:
        i.write(bfile.getvalue())


def resize_and_reduce_brightness(image_name, width, height=None, factor=0.4, quality=75):

    with storage.open(image_name, 'rb') as m:
        im = Image.open(m)
        enhancer = ImageEnhance.Brightness(im)

        if height is None:
            height = int((im.height * width) / im.width)
            size = width, height
        else:
            size = width, height

        im = enhancer.enhance(factor)  # change the brightness
        im = im.resize(size, Image.ANTIALIAS)  # resize the image

        bfile = BytesIO()
        im.save(bfile, format="JPEG", quality=quality,
                optimize=True)  # optimize the image

    with storage.open(image_name, 'wb') as i:
        i.write(bfile.getvalue())


def create_thumbnail(image_name, width, height=None, quality=75, format="JPEG"):
    with storage.open(image_name, 'rb') as m:
        im = Image.open(m)

        if height is None:
            height = int((im.height * width) / im.width)
            size = width, height
        else:
            size = width, height

        im = im.resize(size, Image.ANTIALIAS)

        bfile = BytesIO()
        im.save(bfile, format=format, quality=quality)

    filepath, ext = image_name.split('.')
    filename = f"{filepath}.thumbnail.{ext}"

    with storage.open(filename, 'wb') as i:
        i.write(bfile.getvalue())
