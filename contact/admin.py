from django.contrib import admin

from .models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name", "city", "phone_number", "email", "date_and_time"]
    search_fields = ["full_name", "city", "email"]
    ordering = ("-date_and_time",)
    readonly_fields = [
        "full_name",
        "city",
        "phone_number",
        "email",
        "date_and_time",
        "message",
    ]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "signup_date"]
    search_fields = ["full_name", "email"]
    ordering =("-signup_date",)
    readonly_fields = ["full_name", "email", "signup_date"]
