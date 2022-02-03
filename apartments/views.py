from contact.forms import InquiryForm
from django.views.generic import DetailView, ListView
from django_filters.views import FilterView

from apartments.filters import ApartmentFilter
from apartments.models import Apartment


class ApartmentListView(FilterView):
    queryset = (
        Apartment.objects.all().select_related("agent").prefetch_related("images")
    )
    filterset_class = ApartmentFilter
    paginate_by = 8
    context_object_name = "apartments"


class ApartmentDetailView(DetailView):
    queryset = (
        Apartment.objects.all().select_related("agent").prefetch_related("images")
    )
    context_object_name = "apartment"
    template_name = "apartments/detail-apartment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ask_question_form"] = InquiryForm()
        return context
