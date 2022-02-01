from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["full_name", "city", "phone_number", "email", "date_and_time"]
    search_fields = ["full_name", "city", "email"]
    ordering = ("-date_and_time",)
    readonly_fields = ["full_name", "city", "phone_number", "email", "date_and_time", "message"]
