from django.shortcuts import render, redirect
from .forms import URLShortenerForm
from .models import URLShortener
import string
import random

def generate_shortened_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def shorten_url(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = generate_shortened_url()
            url_shortener = URLShortener(original_url=original_url, shortened_url=shortened_url)
            url_shortener.save()
            return render(request, 'index.html', {'original_url': original_url, 'shortened_url': shortened_url})
    else:
        form = URLShortenerForm()
    return render(request, 'index.html', {'form': form})


def redirect_original_url(request, shortened_part):
    try:
        url_shortener = URLShortener.objects.get(shortened_url=shortened_part)
        original_url = url_shortener.original_url
        return redirect(original_url)
    except URLShortener.DoesNotExist:
        # Handle the case where the shortened URL does not exist
        # You can render a custom 404 page or redirect to a specific view
        pass
