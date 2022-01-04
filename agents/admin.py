from django.contrib import admin

from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "verified",)
    list_filter = ("verified",)
    search_fields = ("full_name",)