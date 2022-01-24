from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ApartmentImage, Apartment
from utils.image_utils import resize_image, create_thumbnail


@receiver(post_save, sender=ApartmentImage)
def reduce_apartment_image_quality_and_optimize(sender, instance, **kwargs):
    """Take a quality factor between 1 to 100 and optimize the image"""
    resize_image(instance.image.name, width=1920, quality=70)


@receiver(post_save, sender=ApartmentImage)
def create_thumbnail_for_first_image(sender, instance, **kwargs):
    if instance == instance.apartment.images.first():
        create_thumbnail(instance.image.name, width=400, height=400)
