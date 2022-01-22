from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_manipulation import reduce_quality, resize_image

from .models import Agent


@receiver(post_save, sender=Agent)
def reduce_agent_picture_quality_and_optimize(sender, instance, **kwargs):
    reduce_quality(instance.picture, instance.picture.name, new_width=720, quality=80)
