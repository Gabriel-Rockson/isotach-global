from django.contrib import admin
from .models import Apartment, ApartmentImage


class ApartmentImageInline(admin.StackedInline):
    model = ApartmentImage
    list_display = ("image", )
    extra = 1
    min_num = 1
    max_num = 15


@admin.register(Apartment)
class ApartmentModel(admin.ModelAdmin):
    list_display = (
        "title",
        "image_tag",
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
        "image_tag",
    )
    inlines = [ApartmentImageInline]
    save_on_top = True
