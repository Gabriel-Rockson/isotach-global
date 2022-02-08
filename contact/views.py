from django.views.generic import TemplateView
from django.views.generic.edit import FormView, ModelFormMixin, View, BaseFormView
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from .forms import ContactForm, NewsletterForm, InquiryForm, ScheduleMeetingForm


# TODO these handle form views do not handle invalid forms
# TODO there is an assumption that the submitted form is valid. 
# TODO find a way to handle the invalid forms and send the errors back to the templates

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


class HandleNewsletterSignupFormView(FormView):
    form_class = NewsletterForm
    success_url = reverse_lazy("contact:newsletter-success")

    def form_valid(self, form):
        form.save()
        
        form.send_admins_mail()
        form.send_mail_to_person()
        
        return super().form_valid(form)


class NewsletterSignupFormSuccessView(TemplateView):
    template_name = "contact/newsletter-success.html"


class HandleInquiryFormView(FormView):
    form_class = InquiryForm
    success_url = reverse_lazy("contact:inquiry-success")

    def form_valid(self, form):
        form.save()
        # TODO Send an email to the person
        return super().form_valid(form)


class InquiryFormSuccessView(TemplateView):
    template_name = "contact/inquiry-success.html"


class HandleScheduleMeetingFormView(FormView):
    form_class = ScheduleMeetingForm
    success_url = reverse_lazy("contact:schedule-meeting-success")
    
    def form_valid(self, form):
        form.save()
        # TODO send an email tot the person
        return super().form_valid(form)
    

class ScheduleMeetingSuccessView(TemplateView):
    template_name = "contact/schedule-meeting-success.html"