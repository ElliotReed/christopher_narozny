from django.contrib.sitemaps import Sitemap

from appearances.models import Appearance
from catalog.models import Book
from news.models import NewsItem


class BookSitemap(Sitemap):
    def items(self):
        return Book.objects.all()


class AppearanceSitemap(Sitemap):
    def items(self):
        return Appearance.objects.all()
