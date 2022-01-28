from pathlib import Path
from django import template

register = template.Library()

from pages.models import HomePage, AboutSection


@register.simple_tag
def get_section_featured_image(section):
    if isinstance(section, HomePage):
        url = Path(section.banner_image.url)
        return {"jpeg": url.with_suffix(".jpg"), "webp": url.with_suffix(".webp")}
    elif isinstance(section, AboutSection):
        url = Path(section.featured_image.url)
        return {"jpeg": url.with_suffix(".jpg"), "webp": url.with_suffix(".webp")}
    return {"jpeg": "Not found", "webp": "Not Found"}
