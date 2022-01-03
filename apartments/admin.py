from django.contrib import admin
from .models import Apartment


@admin.register(Apartment)
class ApartmentModel(admin.ModelAdmin):
    list_display = (
        "title",
        "for_sale",
        "for_rent",
        "bedrooms",
        "baths",
    )
    list_filter = (
        "for_sale",
        "for_rent",
        "bedrooms",
        "baths",
        "self_contained",
        "verified",
    )
    search_fields = (
        "title",
        "description",
        "location",
    )
    readonly_fields = (
        "total_rent_payment",
        "agent_fee",
    )
    save_on_top = True
