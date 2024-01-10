# urls.py in the project directory

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshortener.urls')),  # Include the app's urls with the specified namespace
]
