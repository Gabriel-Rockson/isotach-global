from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.utils.html import mark_safe
from django.urls import reverse
from pathlib import Path


class ApartmentImage(models.Model):
    image = models.ImageField(upload_to="apartment/image/",
                              null=False,
                              blank=False)
    apartment = models.ForeignKey("apartments.Apartment",
                                  on_delete=models.CASCADE,
                                  blank=False,
                                  null=False,
                                  related_name="images")

    def __str__(self):
        return f"{self.image}"


class Apartment(models.Model):
    agent = models.ForeignKey(
        "agents.Agent",
        verbose_name=_("Agent"),
        help_text="Which agent is in charge of this apartment?",
        related_name="apartments",
        on_delete=models.CASCADE,
        null=True,
        blank=False)
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
    featured = models.BooleanField(
        verbose_name=_("Featured Listing"),
        help_text=
        "If this apartment is featured, it is going to be displayed on the homepage and also will be at the top of apartment listings",
        default=False)
    # TODO add major city location, like Kumasi, Accra, e.t.c
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
    monthly_rent_payment = models.FloatField(
        verbose_name=_("Monthly Rent Payment"),
        help_text=
        "How much is a tenant going to pay for the place every month?",
        blank=False,
        null=False)
    description = models.TextField(
        verbose_name=_("Extra Description"),
        help_text=
        "Enter any extra details the potential occupant needs to know",
        blank=True,
        null=True)
    total_rent_payment = models.FloatField(
        verbose_name=_("Total Rent Payment"),
        help_text=
        "Amount tenant will pay over years of residency, monthly_payment * advance_years"
    )
    agent_commission = models.PositiveSmallIntegerField(
        verbose_name=_("Agent's Commission ( percentage )"),
        help_text="What is the commission the agent will take, in percentage.",
        default=5)
    agent_fee = models.FloatField(
        verbose_name="Agent's Fee ( amount )",
        help_text="Amount to pay to the agent.",
        blank=True,
        null=True)
    inspection_fee = models.PositiveSmallIntegerField(
        verbose_name=_("Inspection Fee"),
        help_text=
        "How much is this agent charging potential clients to go show them the place?",
        default=50)
    verified = models.BooleanField(
        verbose_name=_("Verified"),
        help_text="Has this apartment been verified? Tick if Yes",
        default=False)

    def get_absolute_url(self):
        return reverse("apartments:apartment-detail", kwargs={"slug": self.slug})

    def first_image_url(self):
        if self.images:
            return self.images.first().image.url
        else:return 'No Image found'
        
    def first_image_webp_url(self):
        if self.images:
            url = Path(self.images.first().image.url)
            return url.with_suffix('.webp')
        else: return 'No Image Found'

    def images_count(self):
        return self.images.count()

    def get_monthly_rent_payment(self):
        return "{:.2f}".format(self.monthly_rent_payment)

    def get_total_rent_payment(self):
        return "{:.2f}".format(self.total_rent_payment)

    def get_agent_fee(self):
        return "{:.2f}".format(self.agent_fee)
    
    def get_inspection_fee(self):
        return "{:.2f}".format(self.inspection_fee)
    
    def get_number_of_advance_months(self):
        return self.advance_years * 12

    def __str__(self):
        return f"{self.title}"

    def image_tag(self):
        if self.images:
            return mark_safe(
                f'<img src="{self.images.first().image.url}" style="width: 200px; height:200px;" />'
            )
        else:
            return 'No Image Found'

    image_tag.short_description = "Apartment's Image"

    def save(self, *args, **kwargs):
        _total_rent_amount = self.monthly_rent_payment * self.advance_years * 12

        self.agent_fee = self.agent_commission * 0.01 * _total_rent_amount
        self.total_rent_payment = _total_rent_amount

        return super(Apartment, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-upload_time", )
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"