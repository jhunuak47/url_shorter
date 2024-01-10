# views.py

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import URLShortener
from .forms import URLShortenerForm
import shortuuid

def url_shortener(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = shortuuid.uuid()[:8]  # using shortuuid for generating short urls
            url_object = URLShortener(original_url=original_url, short_url=short_url)
            url_object.save()
            return render(request, 'result.html', {'url_object': url_object})
    else:
        form = URLShortenerForm()
    return render(request, 'index.html', {'form': form})

def redirect_original(request, short_url):
    try:
        url_object = URLShortener.objects.get(short_url=short_url)
        url_object.click_count += 1
        url_object.save()
        return redirect(url_object.original_url)
    except URLShortener.DoesNotExist:
        return HttpResponseNotFound("URL not found")
