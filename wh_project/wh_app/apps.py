from django.apps import AppConfig


class WhAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wh_app'

    def ready(self):
        import wh_app.signals
