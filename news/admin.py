from django.contrib import admin
from .models import NewsItemType, NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_type",
        "order",
        "article",
        "host_name",
        "podcast",
    )
    fieldsets = (
        (
            None,
            {
                "fields": ("item_type", "order", "description"),
            },
        ),
        (
            "For print articles",
            {
                "fields": (
                    "article",
                    "article_link",
                    "publisher",
                    "publisher_link",
                ),
            },
        ),
        (
            "For Blog or Youtube",
            {
                "fields": (
                    "host_name",
                    "host_link",
                ),
            },
        ),
        (
            "For Podcast",
            {
                "fields": (
                    "podcast",
                    "podcast_link",
                ),
            },
        ),
    )


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsItemType)
