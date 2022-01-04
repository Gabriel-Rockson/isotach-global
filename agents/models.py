from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Agent(models.Model):
    full_name = models.CharField(verbose_name=_("Full Name"),
                                 max_length=50,
                                 help_text="Name of the Agent",
                                 blank=False,
                                 null=False)
    picture = models.ImageField(verbose_name=_("Agent's Photo"),
                                upload_to="agents/photos/",
                                help_text="Upload an image of the agent",
                                blank=True,
                                null=True)
    email = models.EmailField(verbose_name=_("Email of Agent"),
                              max_length=300,
                              blank=False,
                              null=False)
    phone_number = PhoneNumberField()
    date_joined = models.DateField(
        help_text="What date this this Agent join the agency?")
    verified = models.BooleanField(
        default=False, help_text="Is this agent verified? Tick if yes.")

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        ordering = ("date_joined", )
