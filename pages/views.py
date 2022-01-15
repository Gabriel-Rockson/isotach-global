from .models import HomePage
from apartments.models import Apartment

from django.views.generic import TemplateView, View


class HomePage(TemplateView):
    template_name = "pages/homepage.html"
    # TODO find a better way to get this to load even if the tables don't exist
    extra_context = {
        "homepage": HomePage.objects.first(),
        "featured_apartments": Apartment.objects.filter(featured=True)[:8],
        "latest_apartments": Apartment.objects.all()[:8]
    }

    # def get_context_data(self, *args, **kwargs):
    #     kwargs["homepage"] = HomePage.objects.all()
    #     kwargs["featured_apartments"] = Apartment.objects.filter(featured=True)[:8]
    #     kwargs["latest_apartments"] = Apartment.objects.all()[:8]
    #     return super().get_context_data(*args, **kwargs)