"""This file contains utility functions that can be used to modify images before saving them"""
from pathlib import Path
from PIL import Image

# function to compress image

# function to reduce the brightness of an image

# function to change the formt of an image
def convert_image_to_webp(source):
    """Take the source of an image and convert the image to webP"""
    destination = source.with_suffix(".webp")
    image = Image.open(source)
    image.save(destination, format="webp")

    return destination