from django.db import models
from django.utils import timezone

class URLShortener(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
    
    class Meta:
        app_label = 'urlshortener'
        default_auto_field = 'django.db.models.BigAutoField'
