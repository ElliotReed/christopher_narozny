from .views import AppearanceListView, AppearanceDetailView
from django.urls import path

app_name = "appearances"
urlpatterns = [
    path("<slug:slug>/", AppearanceDetailView.as_view(), name="appearance_detail"),
    path("", AppearanceListView.as_view(), name="appearances"),
]
