from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ContactForm


class HandleContactFormView(FormView):
    """This view handles the form and if it's valid, redirects it to the success page"""
    form_class = ContactForm
    success_url = reverse_lazy("contact:contact-success")
    
    def form_valid(self, form):
        form.save()
        # TODO Send email to the person
        return super().form_valid(form)


class ContactFormSuccessView(TemplateView):
    template_name = "contact/contact-success.html"
