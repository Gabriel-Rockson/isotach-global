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
        i.write(bfile.getbuffer())


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
        i.write(bfile.getbuffer())


def create_thumbnail(image_name, width, height=None, quality=75, format="JPEG"):
    with storage.open(image_name, 'rb') as m:
        im = Image.open(m)

        if height is None:
            height = int((im.height * width) / im.width)
            size = width, height
        else:
            size = width, height

        im = im.resize(size, Image.ANTIALIAS)

        bfile_jpeg = BytesIO()
        im.save(bfile_jpeg, format=format, quality=quality)

        bfile_webp = BytesIO()
        im.save(bfile_webp, format="WEBP", quality=quality)

    filepath, ext = image_name.split('.')
    filename_jpeg = f"{filepath}.thumbnail.{ext}"
    filename_webp = f"{filepath}.thumbnail.webp"

    with storage.open(filename_jpeg, 'wb') as i:
        i.write(bfile_jpeg.getbuffer())

    with storage.open(filename_webp, 'wb') as i:
        i.write(bfile_webp.getbuffer())
