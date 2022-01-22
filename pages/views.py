from .models import HomePage
from apartments.models import Apartment

from django.views.generic import TemplateView, View, DetailView


class HomePageView(TemplateView):
    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homepage"] = HomePage.objects.first()
        context["featured_apartments"] = Apartment.objects.filter(featured=True)[:8]
        context["latest_apartments"] = Apartment.objects.all()[:8]
        return context
