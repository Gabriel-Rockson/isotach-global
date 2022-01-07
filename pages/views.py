from .models import HomePage

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "pages/homepage.html"
    extra_context = {
        "homepage": HomePage.objects.first()
    }