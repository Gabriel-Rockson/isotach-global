from django.urls import path
from .views import HandleContactFormView, ContactFormSuccessView

app_name = "contact"
urlpatterns = [
    path('', HandleContactFormView.as_view(), name="handle-contact"),
    path('success/', ContactFormSuccessView.as_view(), name="contact-success"),
]
