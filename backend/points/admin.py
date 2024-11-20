from django.contrib import admin

from .models import PointOfInterest


@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )

    search_fields = ("name", "category", "description")

    list_filter = ("category", "created_at", "updated_at")

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("General Information", {"fields": ("name", "description", "category")}),
        (
            "Location",
            {
                "fields": ("latitude", "longitude"),
                "description": "Ensure the latitude is between -90 and 90, and longitude is between -180 and 180.",
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    save_on_top = True
    ordering = ("-created_at",)
