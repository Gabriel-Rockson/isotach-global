from pathlib import Path
from django import template

register = template.Library()

from pages.models import HomePage, AboutSection, ServicesSection


@register.simple_tag
def get_section_featured_image(section):
    # print('---------------------------------------------------------------------------------------')
    # print(section)
    # print('---------------------------------------------------------------------------------------')
    if isinstance(section, HomePage):
        print(section)
        url = Path(section.banner_image.url)
        return {
            "webp": url.with_suffix('.webp'),
            "jpeg": url.with_suffix('.jpg'),
        }
    elif isinstance(section, AboutSection) or isinstance(section, ServicesSection):
        url = Path(section.featured_image.url)
        return {
            "webp": url.with_suffix('.webp'),
            "jpeg": url.with_suffix('.jpg'),
        }
    return {
        "webp": None,
        "jpeg": None
    }
