from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _


class BasicContactInformation(models.Model):
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=50,
        null=False,
        blank=False,
    )
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(
        verbose_name=_("Email Address"),
        max_length=300,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True


class Contact(BasicContactInformation):
    city = models.CharField(
        verbose_name=_("City / Town"),
        max_length=100,
        null=False,
        blank=False,
    )
    message = models.TextField(verbose_name=_("Message"), max_length=1000)
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class Newsletter(BasicContactInformation):
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Newsletter Signup"
        verbose_name_plural = "Newsletter Signups"
        

class Inquiry(BasicContactInformation):
    date_submitted = models.DateTimeField(auto_now_add=True)
    question = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"
