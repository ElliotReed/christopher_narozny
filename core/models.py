from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    about_text = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="images", help_text="160px by 160px")
    profile_image_description = models.CharField(
        max_length=50, help_text="Describe the picture"
    )
    current = models.BooleanField(default=False, help_text="One must be checked")

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    note = models.TextField(null=True, blank=True)
    current = models.BooleanField(
        default=False, help_text="One or none may be selected"
    )

    def __str__(self):
        return self.note
