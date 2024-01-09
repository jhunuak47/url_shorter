from django.apps import AppConfig

class UrlshortenerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'urlshortener'

    def ready(self):
        # You can put any logic that needs to run when the app is ready here
        pass
