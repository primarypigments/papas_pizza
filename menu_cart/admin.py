from django.contrib import admin
from .models import MenuItem, CartItem, Cart

class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin interface options for MenuItem model.
    Configures the list display in the admin
    panel to show name, price, and description of menu items.
    """
    list_display = ('name', 'price', 'description')

