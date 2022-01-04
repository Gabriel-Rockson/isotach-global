from django.contrib import admin

from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "image_tag",
        "email",
        "phone_number",
        "verified",
    )
    list_filter = ("verified", )
    search_fields = ("full_name", )
    readonly_fields = ['image_tag']