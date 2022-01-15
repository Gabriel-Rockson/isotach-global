from pathlib import Path
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_manipulation import convert_image_to_webp, resize_image

from apartments.models import ApartmentImage


@receiver(post_save, sender=ApartmentImage)
def convert_apartment_image_to_webp(sender, instance, **kwargs):
    resize_image(Path(instance.image.path), 1280, 1080) # TODO find a better way to resize the images
    jpg_image_path = Path(instance.image.path)
    convert_image_to_webp(jpg_image_path)