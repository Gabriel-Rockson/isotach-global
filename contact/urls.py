from django.urls import path
from .views import (
    HandleContactFormView,
    ContactFormSuccessView,
    HandleNewsletterSignupFormView,
    NewsletterSignupFormSuccessView,
)

app_name = "contact"
urlpatterns = [
    # contact form urls
    path("contact-us/", HandleContactFormView.as_view(), name="handle-contact"),
    path(
        "contact-us/success/", ContactFormSuccessView.as_view(), name="contact-success"
    ),
    # newsletter signup urls
    path(
        "newsletter-signup/",
        HandleNewsletterSignupFormView.as_view(),
        name="handle-newsletter",
    ),
    path(
        "newsletter-signup/success/",
        NewsletterSignupFormSuccessView.as_view(),
        name="newsletter-success",
    ),
]
