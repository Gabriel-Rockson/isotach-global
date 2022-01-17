"""Signal handlers"""
from pathlib import Path

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_manipulation import convert_image_to_webp, change_brightness, resize_image

from .models import AboutSection, HomePage, ServicesSection


# Convert banner image to webp
@receiver(post_save, sender=HomePage)
def convert_homepage_banner_image(sender, instance, **kwargs):
    resize_image(Path(instance.banner_image.path), 2400, 1600)
    jpg_image_path = Path(instance.banner_image.path)
    convert_image_to_webp(jpg_image_path)


# change the brightness of banner image
@receiver(post_save, sender=HomePage)
def change_image_brightness(sender, instance, **kwargs):
    webp_image_path = Path(instance.get_webp_image_path())
    change_brightness(webp_image_path, 0.4)


# convert about section featured image to webp
@receiver(post_save, sender=AboutSection)
def convert_about_section_featured_image(sender, instance, **kwargs):
    resize_image(Path(instance.featured_image.path), 1280, 720)
    jpg_image_path = Path(instance.featured_image.path)
    convert_image_to_webp(jpg_image_path)


# convert services section featured image to webp
@receiver(post_save, sender=ServicesSection)
def convert_services_section_featured_image(sender, instance, **kwargs):
    resize_image(Path(instance.featured_image.path), 1280, 720)
    jpg_image_path = Path(instance.featured_image.path)
    convert_image_to_webp(jpg_image_path)
