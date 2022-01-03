from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField


class Apartment(models.Model):
    # images - foreign key
    # agent - foreign key
    upload_time = models.DateTimeField(verbose_name=_("Date Uploaded"),
                                       auto_now_add=True)
    title = models.CharField(
        verbose_name=("Title"),
        help_text="Example: 3 bedroom apartment at Kumasi, Ghana.",
        max_length=250,
        default="",
        blank=False,
        null=False)
    slug = AutoSlugField(populate_from="title")
    for_sale = models.BooleanField(verbose_name=_("For Sale"),
                                   help_text="Is this apartment for sale?",
                                   default=False)
    for_rent = models.BooleanField(verbose_name=_("For Rent"),
                                   help_text="Is this apartment for rent?",
                                   default=True)
    available = models.BooleanField(
        verbose_name=("Available"),
        help_text="Check this box if the apartment has NOT been rented out.",
        default=True)
    location = models.CharField(verbose_name=_("Location"),
                                help_text="Where is this apartment located?",
                                max_length=50,
                                null=False,
                                blank=False)
    bedrooms = models.PositiveSmallIntegerField(
        verbose_name=_("Number of Bedrooms"),
        help_text="What is the total number of bedrooms in this apartment?",
        default=1)
    baths = models.PositiveSmallIntegerField(
        verbose_name=_("Number of Baths"),
        help_text="How many baths are in this apartment?",
        default=1)
    hall = models.BooleanField(
        verbose_name=_("Hall"),
        help_text="Does this apartment have a hall? Tick if yes.",
        default=False)
    self_contained = models.BooleanField(
        verbose_name=_("Self Contained"),
        help_text="Is this apartment self contained? Tick if yes.",
        default=True)
    advance_years = models.PositiveSmallIntegerField(
        verbose_name=_("Years of Advance Payment"),
        help_text=
        "If this place is being rented out, how many years of advance payment is required?",
        default=1)
    monthly_rent_payment = models.PositiveSmallIntegerField(
        verbose_name=_("Monthly Rent Payment"),
        help_text=
        "How much is a tenant going to pay for the place every month?",
        blank=False,
        null=False)
    description = models.TextField(
        verbose_name=_("Extra Description"),
        help_text="Enter any extra details the potential occupant needs to know"
    )
    total_rent_payment = models.PositiveIntegerField(
        verbose_name=_("Total Rent Payment"),
        help_text=
        "Amount tenant will pay over years of residency, monthly_payment * advance_years"
    )
    agent_commission = models.PositiveSmallIntegerField(
        verbose_name=_("Agent's Commission ( percentage )"),
        help_text="What is the commission the agent will take, in percentage.",
        default=5)
    agent_fee = models.PositiveSmallIntegerField(
        verbose_name="Agent's Fee ( amount )",
        help_text="Amount to pay to the agent.")
    inspection_fee = models.PositiveSmallIntegerField(
        verbose_name=_("Inspectoion Fee"),
        help_text=
        "How much is this agent charging potential clients to go show them the place?",
        default=50)
    verified = models.BooleanField(
        verbose_name=_("Verified"),
        help_text="Has this apartment been verified? Tick if Yes",
        default=False)

    def save(self, *args, **kwargs):
        _total_rent_amount = self.monthly_rent_payment * self.advance_years

        self.agent_fee = self.agent_commission * 0.01 * _total_rent_amount
        self.total_rent_payment = _total_rent_amount

        return super(Apartment, self).save(*args, **kwargs)

    class Meta:
        ordering = ("upload_time", )
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"