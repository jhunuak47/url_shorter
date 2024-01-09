from django.contrib import admin
from .models import URLShortener

# Register the URLShortener model with the admin interface
@admin.register(URLShortener)
class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'shortened_url',)
    search_fields = ('original_url', 'shortened_url')
