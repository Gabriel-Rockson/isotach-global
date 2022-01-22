from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ApartmentImage
from utils.image_manipulation import reduce_quality, resize_image


@receiver(post_save, sender=ApartmentImage)
def reduce_apartment_image_quality_and_optimize(sender, instance, **kwargs):
    """Take a quality factor between 1 to 100 and optimize the image"""
    reduce_quality(instance.image, instance.image.name, new_width=1920, quality=70)
