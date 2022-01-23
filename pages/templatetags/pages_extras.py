from pathlib import Path
from django import template

register = template.Library()


@register.simple_tag
def get_section_featured_image(section):
    print(section)
    if section == 'homepage':
        url = Path(section.banner_image.url)
        print(url)
        return {
            "webp": url.with_suffix('.webp'),
            "jpeg": url.with_suffix('.jpg'),
        }
    elif section == 'homepage.about_section' or section == 'homepage.services_sectoin':
        url = Path(section.featured_image.url)
        print(url)
        return {
            "webp": url.with_suffix('.webp'),
            "jpeg": url.with_suffix('.jpg'),
        }
    return {
        "webp": None,
        "jpeg": None
    }