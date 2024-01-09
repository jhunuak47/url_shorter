from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('<str:shortened_part>/', views.redirect_original_url, name='redirect_original_url'),
]
