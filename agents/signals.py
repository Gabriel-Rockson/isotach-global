from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.image_utils import resize_image

from .models import Agent


@receiver(post_save, sender=Agent)
def reduce_agent_picture_quality_and_optimize(sender, instance, **kwargs):
    resize_image(instance.picture.name, 400)
