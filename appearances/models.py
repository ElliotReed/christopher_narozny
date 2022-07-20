from django.db import models
from django.db.models.deletion import PROTECT


class AppearanceType(models.Model):
    appearance_type = models.CharField(max_length=150)

    def __str__(self):
        return self.appearance_type


class Appearance(models.Model):
    appearance_type = models.ForeignKey(AppearanceType, on_delete=PROTECT)
    date = models.DateField()
    time = models.TimeField()
    venue_name = models.CharField(max_length=150, null=True, blank=True)
    venue_link = models.URLField(null=True, blank=True)
    venue_address = models.CharField(max_length=200, null=True, blank=True)
    host_name = models.CharField(max_length=150, null=True, blank=True)
    host_link = models.URLField(null=True, blank=True)
    conference_name = models.CharField(max_length=200, null=True, blank=True)
    conference_link = models.URLField(null=True, blank=True)
    appearance_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.appearance_type.appearance_type
