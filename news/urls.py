from .views import NewsItemListView
from django.urls import path

app_name = "news"
urlpatterns = [
    path("", NewsItemListView.as_view(), name="news"),
]
