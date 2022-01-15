"""Signal handlers"""
from pathlib import Path

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_manipulation import convert_image_to_webp, change_brightness

from .models import HomePage


@receiver(post_save, sender=HomePage)
def convert_image(sender, instance, **kwargs):
    jpg_image_path = Path(instance.banner_image.path)
    convert_image_to_webp(jpg_image_path)

@receiver(post_save, sender=HomePage)
def change_image_brightness(sender, instance, **kwargs):
    webp_image_path = Path(instance.get_webp_image_path())
    change_brightness(webp_image_path, 0.4)