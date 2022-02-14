from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from contact.models import SiteAdministrator

from .models import Contact, Inquiry, Newsletter, ScheduleMeeting


class ContactForm(forms.ModelForm):
    def send_email_to_admins(self):
        context = {
            "full_name": self.cleaned_data.get("full_name"),
            "phone_number": self.cleaned_data.get("phone_number"),
            "email": self.cleaned_data.get("email"),
            "city": self.cleaned_data.get("city"),
            "message": self.cleaned_data.get("message"),
        }

        email_subject = "CONTACT MESSAGE FROM WEBSITE VISITOR"
        email_body = render_to_string("emails/contact-email-body_admins.txt", context)

        email = EmailMessage(
            email_subject,
            email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[admin.email for admin in SiteAdministrator.objects.all()],
        )
        email.send(fail_silently=False)

    def send_email_to_site_visitor(self):
        context = {
            "full_name": self.cleaned_data.get("full_name"),
            "phone_number": self.cleaned_data.get("phone_number"),
            "email": self.cleaned_data.get("email"),
            "city": self.cleaned_data.get("city"),
            "message": self.cleaned_data.get("message"),
        }

        email_subject = "THANKS FOR CONTACTING US"
        email_body = render_to_string(
            "emails/contact-email-body_site-visitor.txt", context
        )

        email = EmailMessage(
            email_subject,
            email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[context["email"]],
        )
        email.send(fail_silently=False)

    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    def send_email_to_admins(self):
        context = {
            "full_name": self.cleaned_data.get("full_name"),
            "email": self.cleaned_data.get("email"),
        }

        email_subject = "SIGNUP FOR NEWSLETTER"
        email_body = render_to_string("emails/newsletter-email-body_admins.txt", context)
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[admin.email for admin in SiteAdministrator.objects.all()],
        )
        email.send(fail_silently=False)

    def send_email_to_site_visitor(self):
        context = {
            "full_name": self.cleaned_data.get("full_name"),
            "email": self.cleaned_data.get("email"),
        }

        email_subject = "THANKS FOR SIGNING UP FOR OUR NEWSLETTER"
        email_body = render_to_string("emails/newsletter-email-body_site-visitor.txt", context)
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[context["email"]],
        )
        email.send(fail_silently=False)

    class Meta:
        model = Newsletter
        fields = "__all__"


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"


class ScheduleMeetingForm(forms.ModelForm):
    class Meta:
        model = ScheduleMeeting
        fields = "__all__"
