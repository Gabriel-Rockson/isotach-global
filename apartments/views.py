from django.shortcuts import render
from django.views.generic import ListView

from apartments.models import Apartment


class ApartmentListView(ListView):
    queryset = Apartment.objects.all()
    context_object_name= "apartments"
    template_name = "apartments/list-apartments.html"