from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScrapingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello_api.scraping'
    verbose_bane = _("Scraping")

    def ready(self):
        try:
            import hello_api.scraping.signals  # noqa F401
        except ImportError:
            pass
