from django.core.files.storage import default_storage as storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from pages.models import HomePage


@receiver(post_save, sender=HomePage)
def resize_homepage_banner_image(sender, instance, **kwargs):
    image = Image.open(instance.banner_image)
    resized_image = image.resize((1280, 720), Image.ANTIALIAS)

    fh = storage.open(instance.banner_image.name, 'wb')
    picture_format = 'JPEG'
    resized_image.save(fh, picture_format)
    fh.close()