from django.contrib import admin
from .models import AboutSection, ServicesSection, Service


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1
    min_num = 1
    max_num = 4

@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        ServiceInline,
    ]
