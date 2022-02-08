from .models import HomePage
from apartments.models import Apartment
from agents.models import Agent

from django.views.generic import TemplateView, View, DetailView
from contact.forms import ContactForm


class HomePageView(TemplateView):
    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homepage"] = HomePage.objects.prefetch_related(
            "about_section", "services", "frequently_asked_questions"
        ).first()
        context["featured_apartments"] = (
            Apartment.objects.select_related("agent")
            .prefetch_related("images")
            .filter(featured=True)[:8]
        )
        context["latest_apartments"] = (
            Apartment.objects.select_related("agent")
            .prefetch_related("images")
            .all()[:8]
        )
        context["agents"] = Agent.objects.all()[:8]
        context["contact_form"] = ContactForm()
        return context
