from . import views
from django.urls import path

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("newsletter/", views.newsletter, name="newsletter"),
]
