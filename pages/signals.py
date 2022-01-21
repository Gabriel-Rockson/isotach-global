from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import HomePage
from utils.image_manipulation import resize_image


@receiver(post_save, sender=HomePage)
def resize_homepage_banner_image(sender, instance, **kwargs):
    resize_image(instance.banner_image, instance.banner_image.name, 1280, 720)
