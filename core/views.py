from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from decouple import config


def home(request):
    form = NewsletterForm()

    context = {"form": form}
    return render(request, "core/home.html", context)


def contact(request):
    form = ContactForm()
    response = ""

    if request.method == "POST":
        body = request.POST
        name = body.get("name")
        message = body.get("message")
        sender_email = body.get("email")
        msg_html = render_to_string(
            "core/email.html",
            {"message": {"message": message, "name": name, "sender": sender_email}},
        )

        send_mail(
            f"A new message from {body.get('name')}",
            body.get("message"),
            body.get("email"),
            ["dev@elliotreed.net"],
            html_message=msg_html,
        )
        response = "Your message has been sent, I'll contact you shortly."

    context = {"form": form, "response": response}
    return render(request, "core/contact.html", context)


def about(request):
    return render(request, "core/about.html")


def newsletter(request):
    return render(request, "core/newsletter.html")
