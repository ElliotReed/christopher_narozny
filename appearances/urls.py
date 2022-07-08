from . import views
from django.urls import path

app_name = "appearances"
urlpatterns = [
    path("", views.appearances, name="appearances"),
]
