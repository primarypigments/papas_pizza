from django.contrib import admin
from .models import MenuItem, CartItem, Cart

class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin interface options for MenuItem model.
    Configures the list display in the admin
    panel to show name, price, and description of menu items.
    """
    list_display = ('name', 'price', 'description')


# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.TabularInline
class CartItemInline(admin.TabularInline):
    """
    Defines how CartItem instances are displayed within the Cart admin page.
    Uses a tabular inline layout to show items, quantity,
    and subtotal, with subtotal as a read-only field.
    """
    model = CartItem
    extra = 0
    fields = ['item', 'quantity', 'subtotal']
    readonly_fields = ['subtotal']


class CartAdmin(admin.ModelAdmin):
    """
    Admin interface options for Cart model.
    Configures list display to show user, a comma-separated
    list of added items, total quantity of items, and total price.
    Includes CartItemInline to manage cart
    items within the cart's admin view.
    """
    list_display = ('user', 'display_added_items', 'total_quantity', 'total_price')
    inlines = [CartItemInline]


    def display_added_items(self, obj):
        """
        Returns a comma-separated string of item
        names in the cart for display in the admin list.
        """
        return ', '.join([item.item.name for item in obj.items.all()])


    def total_quantity(self, obj):
        """
        Returns the total quantity of all items
        in the cart for display in the admin list.
        """
        return sum(item.quantity for item in obj.items.all())


    def total_price(self, obj):
        """
        Calls the total_price method of Cart model
        to get the total price of all items in the cart.
        Used in the admin list display.
        """
        return obj.total_price()

