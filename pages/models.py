from pathlib import Path
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from utils.image_manipulation import convert_image_to_webp


class HomePage(models.Model):
    name = models.CharField(
        verbose_name=_("Name of Page"),
        help_text="Enter the name of this page, e.g HomePage",
        max_length=20,
        null=False,
        blank=False,
        default="")
    banner_image = models.ImageField(
        upload_to="featured_images/homepage/",
        verbose_name=_("Banner Image"),
        help_text=
        "Choose an image that will be featured on the banner of the homepage",
        null=False,
        blank=False,
    )
    banner_heading_text = models.CharField(
        verbose_name=_("Banner Heading Text"),
        help_text=
        "Enter the text that will be displayed boldly on the banner on the homepage",
        null=False,
        blank=False,
        default="Discover Your Perfect Home",
        max_length=100)
    banner_sub_heading_text = models.CharField(
        verbose_name=_("Banner Sub Heading Text"),
        help_text=
        "Enter the text that will be displayed below the bold text on the banner",
        null=False,
        blank=False,
        default="Search nearby for apartments, and homes for rent.",
        max_length=130)

    def get_webp_image_path(self):
        path = Path(self.banner_image.path)
        return path.with_suffix('.webp')

    def get_webp_image_url(self):
        url = Path(self.banner_image.url)
        return url.with_suffix('.webp')

    def __str__(self):
        return self.name


class AboutSection(models.Model):
    page = models.ForeignKey("pages.HomePage",
                             on_delete=models.CASCADE,
                             related_name="about_section",
                             default="")
    name = models.CharField(verbose_name=_("Name of Section"),
                            max_length=10,
                            blank=False,
                            null=False,
                            default="")
    featured_image = models.ImageField(verbose_name=_("Featured Image"),
                                       upload_to="featured_images/about/",
                                       null=False,
                                       blank=False)
    heading = models.CharField(
        verbose_name=_("Heading of About"),
        max_length=200,
        help_text=
        "Heading to display on the about section, this can be the name of the company. e.g Isotach Global",
        blank=False,
        null=False,
        default="")
    about_company = models.TextField(
        verbose_name=_("About Company"),
        null=False,
        blank=False,
        help_text=
        "Enter text to tell visitors what this company is about, a little background story"
    )

    def __str__(self):
        return f"{self.about_company[:20]}"


class Service(models.Model):
    name = models.CharField(verbose_name=_("Name of Service"),
                            help_text="Enter the name of the service",
                            null=False,
                            blank=False,
                            max_length=100)
    slug = AutoSlugField(populate_from="name")
    service_section = models.ForeignKey("pages.ServicesSection",
                                        verbose_name=("Service Section"),
                                        related_name="services",
                                        on_delete=models.CASCADE,
                                        blank=False,
                                        null=False)

    def __str__(self):
        return f"{self.name}"


class ServicesSection(models.Model):
    page = models.ForeignKey("pages.HomePage",
                             on_delete=models.CASCADE,
                             related_name="services_section",
                             default="")
    name = models.CharField(verbose_name=_("Name of Section"),
                            max_length=10,
                            blank=False,
                            null=False,
                            default="")

    featured_image = models.ImageField(verbose_name=_("Featured Image"),
                                       upload_to="featured_images/services/",
                                       null=False,
                                       blank=False)
    description = models.TextField(
        verbose_name=_("Brief Description of Services"),
        null=False,
        blank=False,
        help_text=
        "Enter text to tell visitors what this company is about, a little background story"
    )

    def __str__(self):
        return f"{self.description[:30]}"


class FrequentlyAskedQuestion(models.Model):
    page = models.ForeignKey("pages.HomePage",
                             related_name="frequently_asked_questions",
                             on_delete=models.CASCADE)
    question = models.CharField(
        verbose_name=_("Question"),
        max_length=300,
        help_text="Enter the question",
        blank=False,
        null=False,
    )
    answer = models.TextField(verbose_name=_("Answer"),
                              help_text="Enter the answer to this question",
                              blank=False,
                              null=False)
