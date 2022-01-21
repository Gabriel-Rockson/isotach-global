from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import HomePage
from utils.image_manipulation import resize_image, convert_to_webp, convert_image_to_webp

from pathlib import Path


@receiver(post_save, sender=HomePage)
def resize_homepage_banner_image_and_convert_to_webp(sender, instance, **kwargs):
    resize_image(instance.banner_image, instance.banner_image.name, 1280, 720)
    # convert_to_webp(instance.banner_image, instance.banner_image.name)
    convert_image_to_webp(Path(instance.banner_image.path))