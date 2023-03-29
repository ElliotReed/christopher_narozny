from django.contrib import admin
from .models import Appearance, AppearanceType


class AppearanceAdmin(admin.ModelAdmin):

    list_display = ("appearance_type", "date", "host_name", "conference_name")
    fieldsets = (
        (
            None,
            {
                "fields": ("appearance_type", "appearance_details", "slug"),
            },
        ),
        (
            "Date and Time",
            {
                "fields": (
                    "date",
                    "time",
                ),
            },
        ),
        (
            "For Book signing, In conversation with, Conference",
            {
                "fields": (
                    "venue_name",
                    "venue_link",
                    "venue_address",
                ),
            },
        ),
        (
            "For Facebook live, In conversation with",
            {"fields": ("host_name", "host_link")},
        ),
        ("For Conference", {"fields": ("conference_name", "conference_link")}),
    )
    prepopulated_fields = {"slug": ("date", "time")}


admin.site.register(Appearance, AppearanceAdmin)
admin.site.register(AppearanceType)

# Register your models here.
