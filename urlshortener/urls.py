# urls.py in urlshortener app

from django.urls import path
from . import views

app_name = 'urlshortener'  # Set the application namespace

urlpatterns = [
    path('', views.url_shortener, name='url_shortener'),
    path('<str:short_url>/', views.redirect_original, name='redirect_original'),
]
