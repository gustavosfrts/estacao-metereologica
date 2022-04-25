from django.apps import AppConfig


class SensoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensores'

    def ready(self):
        from forecastUpdater import updater
        updater.start()