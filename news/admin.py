from django.contrib import admin
from .models import NewsItemType, NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_type",
        "order",
        "article",
        "host_name",
        "podcast",
        "publisher",
    )


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsItemType)
