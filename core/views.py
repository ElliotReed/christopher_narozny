from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from .models import Author, Newsletter
from catalog.models import Book
from .email import add_subscriber, send_contact_form


def add_current_newsletter_note_if_exists(context):
    newsletter_note = Newsletter.objects.filter(current=True)
    if newsletter_note:
        current_note = newsletter_note[0]
        context["newsletter_note"] = current_note
        return context


def about(request):
    authors = Author.objects.filter(current=True)
    author = authors[0]
    context = {"author": author}
    return render(request, "core/about.html", context)


def contact(request):
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()

    if request.method == "POST":
        if "contact" in request.POST:
            send_contact_form(request)

        if "newsletter" in request.POST:
            subscriber_email = request.POST.get("subscriber_email")
            add_subscriber(request, subscriber_email)

    context = {
        "contact_form": contact_form,
        "newsletter_form": newsletter_form,
    }

    add_current_newsletter_note_if_exists(context)

    return render(request, "core/contact.html", context)


def home(request):
    book = Book.objects.get(featured=True)
    newsletter_form = NewsletterForm()

    if request.method == "POST":
        subscriber_email = request.POST.get("subscriber_email")
        add_subscriber(request, subscriber_email)

    context = {
        "book": book,
        "newsletter_form": newsletter_form,
    }

    add_current_newsletter_note_if_exists(context)

    return render(request, "core/home.html", context)


def newsletter(request):
    author = Author.objects.get(id=1)
    newsletter_form = NewsletterForm()

    if request.method == "POST":
        subscriber_email = request.POST.get("subscriber_email")
        add_subscriber(request, subscriber_email)

    context = {
        "newsletter_form": newsletter_form,
        "author": author,
    }

    add_current_newsletter_note_if_exists(context)

    return render(request, "core/newsletter.html", context)
