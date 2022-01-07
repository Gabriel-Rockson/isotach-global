from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import (AboutSection, FrequentlyAskedQuestion, HomePage, Service,
                     ServicesSection)


class FrequentlyAskedQuestionInline(admin.StackedInline):
    model = FrequentlyAskedQuestion
    extra = 1
    min_num = 1

class AboutSectionInline(admin.StackedInline):
    model = AboutSection
    extra = 0
    min_num = 1
    max_num = 1


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1
    min_num = 1
    max_num = 4


class ServicesSectionInline(admin.StackedInline):
    model = ServicesSection
    extra = 0
    min_num = 1
    max_num = 1
    # TODO find a way to add inlines to this inline


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("name", )
    inlines = [AboutSectionInline, ServicesSectionInline, FrequentlyAskedQuestionInline]

    def add_view(self, request, *args, **kwargs):
        if request.method == "POST":
            if HomePage.objects.count() > 0:
                # TODO redirect the user to a page that shows them they can't create a new homepage
                return HttpResponseRedirect(reverse("admin:index"))
        return super(HomePageAdmin, self).add_view(request, *args, **kwargs)
