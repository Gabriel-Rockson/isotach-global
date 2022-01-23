from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import HomePage, AboutSection, ServicesSection
from utils.image_manipulation import resize_image, reduce_brightness, reduce_quality

from pathlib import Path


@receiver(post_save, sender=HomePage)
def reduce_quality_homepage_banner_image(sender, instance, **kwargs):
    reduce_quality(instance.banner_image,
                   instance.banner_image.name, new_width=1920)


@receiver(post_save, sender=HomePage)
def reduce_brightness_of_homepage_banner_image(sender, instance, **kwargs):
    reduce_brightness(instance.banner_image, instance.banner_image.name, 0.3)


@receiver(post_save, sender=AboutSection)
def reduce_quality_about_section_featured_image(sender, instance, **kwargs):
    reduce_quality(instance.featured_image,
                   instance.featured_image.name, new_width=720, quality=65)


@receiver(post_save, sender=ServicesSection)
def reduce_quality_services_section_featured_image(sender, instance, **kwargs):
    reduce_quality(instance.featured_image,
                   instance.featured_image.name, new_width=720, quality=65)
