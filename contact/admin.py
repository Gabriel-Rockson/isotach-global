from django.contrib import admin

from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["full_name", "city", "phone_number", "email", "date_and_time"]
    search_fields = ["full_name", "city", "email"]
    ordering = ("-date_and_time",)
