from django.db import models

class URLShortener(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.original_url
