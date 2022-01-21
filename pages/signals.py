from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import HomePage
from utils.image_manipulation import resize_image, reduce_brightness

from pathlib import Path


@receiver(post_save, sender=HomePage)
def resize_homepage_banner_image(sender, instance, **kwargs):
    resize_image(instance.banner_image, instance.banner_image.name, 2400, 1600)


@receiver(post_save, sender=HomePage)
def reduce_brightness_of_homepage_banner_image(sender, instance, **kwargs):
    reduce_brightness(instance.banner_image, instance.banner_image.name, 0.4)