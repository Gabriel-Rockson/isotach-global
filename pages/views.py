from .models import HomePage
from apartments.models import Apartment

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "pages/homepage.html"
    extra_context = {
        "homepage": HomePage.objects.first(),
        "featured_apartments": Apartment.objects.filter(featured=True)[:8],
        "latest_apartments": Apartment.objects.all()[:8]
    }