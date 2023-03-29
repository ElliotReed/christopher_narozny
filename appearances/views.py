from django.views.generic import ListView, DetailView
from .models import Appearance
from catalog.models import Book
from core.models import Author


class AppearanceListView(ListView):
    model = Appearance
    context_object_name = "appearances"
    template_name = "appearances/appearances.html"
    ordering = ["-date", "-time"]

    def get_context_data(self):
        context = super().get_context_data()
        author = Author.objects.get(id=1)
        book = Book.objects.get(featured=True)
        context["book"] = book
        context["author"] = author
        return context


class AppearanceDetailView(DetailView):
    model = Appearance
    context_object_name = "appearance"
    template_name = "appearances/appearance_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        author = Author.objects.get(id=1)
        book = Book.objects.get(featured=True)
        context["book"] = book
        context["author"] = author
        return context
