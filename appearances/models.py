from django.db import models
from django.db.models.deletion import PROTECT
from django.urls import reverse


class AppearanceType(models.Model):
    appearance_type = models.CharField(max_length=150)

    class Meta:
        ordering = ("appearance_type",)

    def __str__(self):
        return self.appearance_type


class Appearance(models.Model):
    appearance_type = models.ForeignKey(AppearanceType, on_delete=PROTECT)
    date = models.DateField()
    time = models.TimeField(
        help_text="Time is eastern standard time, 24 hour format eg. '18:00:00'"
    )
    venue_name = models.CharField(max_length=150, null=True, blank=True)
    venue_link = models.URLField(null=True, blank=True)
    venue_address = models.CharField(max_length=200, null=True, blank=True)
    host_name = models.CharField(max_length=150, null=True, blank=True)
    host_link = models.URLField(null=True, blank=True)
    conference_name = models.CharField(max_length=200, null=True, blank=True)
    conference_link = models.URLField(null=True, blank=True)
    appearance_details = models.TextField(null=True, blank=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text="Automatically generated from date and time",
    )

    def __str__(self):
        return self.appearance_type.appearance_type

    def get_absolute_url(self):
        return reverse("appearances:appearance_detail", kwargs={"slug": self.slug})
