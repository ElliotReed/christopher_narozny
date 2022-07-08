from . import views
from django.urls import path

app_name = "catalog"
urlpatterns = [
    path("", views.catalog, name="catalog"),
]
