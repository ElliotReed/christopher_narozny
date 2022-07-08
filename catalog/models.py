from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    # large_image = models.ImageField()
    # small_image = models.ImageField()

    def __str__(self):
        return self.title
