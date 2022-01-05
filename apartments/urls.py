from django.urls import path

from .views import ApartmentListView

app_name = "apartments"
urlpatterns = [
    path('', ApartmentListView.as_view(), name="list-apartments"),
]
