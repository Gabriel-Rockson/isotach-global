from django.urls import path

from .views import HomePageView, ImageSliderView

app_name="pages"
urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('image-slider/', ImageSliderView.as_view(), name="image-slider")
]
