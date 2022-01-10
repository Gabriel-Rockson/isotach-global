from django.urls import path

from .views import ApartmentDetailView, ApartmentListView

app_name = "apartments"
urlpatterns = [
    path('', ApartmentListView.as_view(), name="list-apartments"),
    path('<slug:slug>/', ApartmentDetailView.as_view(), name="apartment-detail"),
]
