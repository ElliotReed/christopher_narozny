from django.db import models
from django.db.models.deletion import PROTECT


class NewsItemType(models.Model):
    item_type = models.CharField(max_length=150)

    def __str__(self):
        return self.item_type


class NewsItem(models.Model):
    item_type = models.ForeignKey(NewsItemType, on_delete=PROTECT)
    order = models.IntegerField()
    article = models.CharField(max_length=150, null=True, blank=True)
    article_link = models.URLField(null=True, blank=True)
    host_name = models.CharField(max_length=150, null=True, blank=True)
    host_link = models.URLField(null=True, blank=True)
    podcast = models.CharField(max_length=200, null=True, blank=True)
    podcast_link = models.URLField(null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    publisher_link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item_type.item_type
