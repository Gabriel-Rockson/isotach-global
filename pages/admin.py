from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import AboutSection, FrequentlyAskedQuestion, HomePage, Service


class FrequentlyAskedQuestionInline(admin.StackedInline):
    model = FrequentlyAskedQuestion
    min_num = 1
    extra = 0


class AboutSectionInline(admin.StackedInline):
    model = AboutSection
    extra = 0
    min_num = 1
    max_num = 1


class ServiceInline(admin.StackedInline):
    model = Service
    min_num = 1
    extra = 0
    max_num = 4


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    save_on_top = True
    inlines = [AboutSectionInline, ServiceInline, FrequentlyAskedQuestionInline]

    def add_view(self, request, *args, **kwargs):
        if request.method == "POST":
            if HomePage.objects.count() > 0:
                # TODO redirect the user to a page that shows them they can't create a new homepage
                return HttpResponseRedirect(reverse("admin:index"))
        return super(HomePageAdmin, self).add_view(request, *args, **kwargs)
