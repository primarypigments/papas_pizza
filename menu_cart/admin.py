from django.contrib import admin
from .models import MenuItem, CartItem, Cart, Topping


class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin interface options for MenuItem model.
    Configures the list display in the admin
    panel to show name, price, and description of menu items.
    """
    list_display = ('name', 'price', 'description')


class CartItemInline(admin.TabularInline):
    """
    Defines how CartItem instances are displayed within the Cart admin page.
    Uses a tabular inline layout to show items, quantity,
    and subtotal, with subtotal as a read-only field.
    """
    model = CartItem
    extra = 0
    fields = ['item', 'quantity', 'subtotal', 'toppings']
    readonly_fields = ['subtotal']


class CartAdmin(admin.ModelAdmin):
    """
    Admin interface options for Cart model.
    Configures list display to show user, a comma-separated
    list of added items, total quantity of items, and total price.
    Includes CartItemInline to manage cart
    items within the cart's admin view.
    """
    list_display = (
        'user', 'display_added_items',
        'total_quantity', 'total_price', 'created_at')
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

    display_added_items.short_description = 'Added Items'
    total_quantity.short_description = 'Total Quantity'
    total_price.short_description = 'Total Price'


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Topping)
