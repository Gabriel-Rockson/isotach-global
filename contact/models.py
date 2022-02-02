from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=50,
        help_text="Enter your full name",
        null=False,
        blank=False,
    )
    city = models.CharField(
        verbose_name=_("City / Town"),
        max_length=100,
        help_text="Enter your city or town",
        null=False,
        blank=False,
    )
    phone_number = PhoneNumberField()
    email = models.EmailField(
        verbose_name=_("Email Address"),
        help_text="Enter your email address",
        max_length=300,
        blank=False,
        null=False,
    )
    message = models.TextField(
        verbose_name=_("Message"), help_text="Enter your message", max_length=1000
    )
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class Newsletter(models.Model):
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=50,
        help_text="Enter your full name",
        null=False,
        blank=False,
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        help_text="Enter your email address",
        max_length=300,
        blank=False,
        null=False,
    )
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Newsletter Signup"
        verbose_name_plural = "Newsletter Signups"
