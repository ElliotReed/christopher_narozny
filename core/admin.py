from django.contrib import admin
from .models import Author, Newsletter


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "current",
    )


admin.site.register(Author, AuthorAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "note",
        "current",
    )


admin.site.register(Newsletter, NewsletterAdmin)
