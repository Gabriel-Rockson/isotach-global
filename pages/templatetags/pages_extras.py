from pathlib import Path
from django import template

register = template.Library()

from pages.models import HomePage, AboutSection, ServicesSection


@register.simple_tag
def get_section_featured_image(section):
    if isinstance(section, HomePage):
        return {
            "jpeg": section.banner_image.url,
        }
    elif isinstance(section, AboutSection) or isinstance(section, ServicesSection):
        return {
            "jpeg": section.featured_image.url,
        }
    return {
        "jpeg": None
    }
