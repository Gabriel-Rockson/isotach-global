from django.apps import AppConfig


class ApartmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apartments'

    def ready(self):
        import apartments.signals