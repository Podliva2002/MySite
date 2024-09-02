from django.apps import AppConfig


class SiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_app'
    verbose_name = 'Магазин'

    def ready(self):
        from site_app import signals

        print("Inited signals for site_app:", signals.__name__)
