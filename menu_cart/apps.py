from django.apps import AppConfig

class MenuCartConfig(AppConfig):
    """
    Application configuration for the 'menu_cart' app.
    Sets up the default field type for
    auto-created primary key fields to BigAutoField.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu_cart'
    