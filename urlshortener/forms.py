from django import forms
from .models import URLShortener

class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortener
        fields = ['original_url']
        labels = {
            'original_url': 'Original URL'
        }
