from . import views
from django.urls import path

app_name = "news"
urlpatterns = [
    path("", views.news, name="news"),
]
