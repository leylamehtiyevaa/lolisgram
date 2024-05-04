from django.apps import AppConfig


class LolisgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lolisgram'

    def ready(self):
        import lolisgram.signals
