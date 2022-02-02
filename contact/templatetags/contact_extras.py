from contact.forms import NewsletterForm
from django import template

register = template.Library()


@register.simple_tag
def newsletter_form():
    return NewsletterForm()
