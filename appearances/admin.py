from django.contrib import admin
from .models import Appearance, AppearanceType


class AppearanceAdmin(admin.ModelAdmin):
    list_display = ("appearance_type", "date", "host_name", "conference_name")


admin.site.register(Appearance, AppearanceAdmin)
admin.site.register(AppearanceType)

# Register your models here.
