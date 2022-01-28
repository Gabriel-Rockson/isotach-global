from pathlib import Path
from django import template

register = template.Library()

from pages.models import HomePage, AboutSection


@register.simple_tag
def get_section_featured_image(section):
    if isinstance(section, HomePage):
        
        url = section.banner_image.url
        parts = url.split(".jpg")
        webp_url = parts[0] + ".webp"
        
        return {"jpeg": url, "webp": webp_url}
    elif isinstance(section, AboutSection):
        
        url = section.featured_image.url
        parts = url.split(".jpg")
        webp_url = parts[0] + ".webp"
        
        return {"jpeg": url, "webp": webp_url}
    return {"jpeg": "Not found", "webp": "Not Found"}
