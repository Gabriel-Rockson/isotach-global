from io import BytesIO

from django.core.files.storage import default_storage as storage
from PIL import Image, ImageEnhance


# resize image
def resize_image(image_name, width, height=None):
    m = storage.open(image_name, 'rb')
    im = Image.open(m)

    # resizing
    if height is None:
        height = int((im.height * width) / im.width)
        size = width, height
    else:
        size = width, height

    im = im.resize(size, Image.ANTIALIAS)

    bfile = BytesIO()
    im.save(bfile, format="JPEG")

    m.close()

    i = storage.open(image_name, 'wb')
    i.write(bfile.getvalue())

    i.close()


# reduce image brightness
def reduce_brightness(image_name, factor=0.4):
    m = storage.open(image_name, 'rb')
    im = Image.open(m)

    # change brightness
    enhancer = ImageEnhance.Brightness(im)
    im = enhancer.enhance(factor)

    bfile = BytesIO()
    im.save(bfile, format="JPEG")

    m.close()

    i = storage.open(image_name, 'wb')
    i.write(bfile.getvalue())

    i.close()


def resize_and_reduce_brightness(image_name, width, height=None, factor=None, quality=75):

    m = storage.open(image_name, 'rb')
    im = Image.open(m)

    # resizing
    if height is None:
        height = int((im.height * width) / im.width)
        size = width, height
    else:
        size = width, height

    # change brightness
    enhancer = ImageEnhance.Brightness(im)
    im = enhancer.enhance(factor)

    im = im.resize(size, Image.ANTIALIAS)

    bfile = BytesIO()
    im.save(bfile, format="JPEG", quality=quality,
            optimize=True)  # optimize the image

    m.close()

    i = storage.open(image_name, 'wb')
    i.write(bfile.getvalue())

    i.close()

# reduce image quality


# save image
