from django.apps import AppConfig


class AppLabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_lab'

def ready(self):
    import app_lab.signals
