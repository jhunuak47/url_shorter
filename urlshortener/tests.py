# FILEPATH: /C:/Users/hp/OneDrive/Desktop/urlshorter/urlshortener/tests.py
from django.test import TestCase, RequestFactory
from django.shortcuts import redirect
from .models import URLShortener
from .views import redirect_original_url

class URLShortenerTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.shortened_part = 'testurl'
        self.original_url = 'http://www.test.com'
        URLShortener.objects.create(shortened_url=self.shortened_part, original_url=self.original_url)

    def test_redirect_original_url(self):
        request = self.factory.get('/')
        response = redirect_original_url(request, self.shortened_part)
        self.assertEqual(response.url, self.original_url)

    def test_redirect_original_url_does_not_exist(self):
        request = self.factory.get('/')
        response = redirect_original_url(request, 'nonexistenturl')
        self.assertEqual(response, None)