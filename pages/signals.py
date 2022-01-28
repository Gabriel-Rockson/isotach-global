from pathlib import Path

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_utils import resize_image, resize_and_reduce_brightness

from pages.models import AboutSection, HomePage


@receiver(post_save, sender=HomePage)
def resize_and_reduce_brightness_homepage_banner_image(sender, instance, **kwargs):
    resize_and_reduce_brightness(instance.banner_image.name, width=1600, factor=0.4)


@receiver(post_save, sender=AboutSection)
def reduce_quality_about_section_featured_image(sender, instance, **kwargs):
    resize_image(instance.featured_image.name, width=1024, quality=75)
