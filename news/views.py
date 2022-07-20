from django.views.generic import ListView
from .models import NewsItem
from catalog.models import Book
from core.models import Author


class NewsItemListView(ListView):
    model = NewsItem
    context_object_name = "news"
    template_name = "news/news.html"
    ordering = [
        "order",
    ]

    def get_context_data(self):
        context = super().get_context_data()
        author = Author.objects.get(id=1)
        book = Book.objects.get(featured=True)
        context["book"] = book
        context["author"] = author
        return context
