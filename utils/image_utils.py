from io import BytesIO

from django.core.files.storage import default_storage as storage
from PIL import Image, ImageEnhance


# resize image
def resize_image(image_name, width, height=None, quality=None, format="JPEG"):
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


def resize_and_reduce_brightness(image_name, width, height=None, factor=None, quality=75):

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


# reduce image quality


# save image
