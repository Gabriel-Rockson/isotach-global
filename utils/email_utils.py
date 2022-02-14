from django.core.mail import EmailMessage
from contact.models import SiteAdministrator
from django.conf import settings


def send_admin_email(email_subject, email_body):
    email = EmailMessage(
        email_subject,
        email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[admin.email for admin in SiteAdministrator.objects.all()],
    )
    email.send(fail_silently=False)


def send_site_visitor_email(email_subject, email_body, email_address):
    email = EmailMessage(
        email_subject,
        email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[
            email_address,
        ],
    )
    email.send(fail_silently=False)
