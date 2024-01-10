# forms.py

from django import forms
from .models import URLShortener

class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortener
        fields = ['original_url']  # You can specify the fields you want to include in the form and their order
