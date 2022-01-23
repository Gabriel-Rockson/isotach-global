from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apartments.filters import ApartmentFilter
from django_filters.views import FilterView

from apartments.models import Apartment


class ApartmentListView(FilterView):
    filterset_class = ApartmentFilter
    paginate_by = 4
    context_object_name = "apartments"


class ApartmentDetailView(DetailView):
    queryset = Apartment.objects.all()
    context_object_name = "apartment"
    template_name = "apartments/detail-apartment.html"