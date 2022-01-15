"""This file contains utility functions that can be used to modify images before saving them"""
from pathlib import Path
from PIL import Image, ImageEnhance


def resize_image(source, width, height):
    image = Image.open(source)
    new_image = image.resize((width, height))
    new_image.save(source, quality=75, optimize=True)


# function to change the formt of an image
def convert_image_to_webp(source):
    """Take the source of an image and convert the image to webP"""
    destination = source.with_suffix(".webp")
    image = Image.open(source)
    image.save(destination, format="webp", quality=75)


def change_brightness(source, factor):
    """Take the source of an image and change it's brightness by a factor"""
    destination = source.with_suffix(".webp")
    image = Image.open(source)
    enhancer = ImageEnhance.Brightness(image)
    new_img = enhancer.enhance(factor)
    new_img.save(destination)