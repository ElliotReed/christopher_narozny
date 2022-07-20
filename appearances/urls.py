from .views import AppearanceListView
from django.urls import path

app_name = "appearances"
urlpatterns = [
    path("", AppearanceListView.as_view(), name="appearances"),
]
