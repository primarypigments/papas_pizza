from django.apps import AppConfig


class YourAppConfig(AppConfig):
    """
    Application configuration for the 'index' app.
    """
    name = 'index'

    def ready(self):
        """
        Imports signal handlers upon app readiness.
        """
        import your_app.signals


class IndexConfig(AppConfig):
    """
    Configures settings for the 'index'
    application, using BigAutoField for ID fields.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
