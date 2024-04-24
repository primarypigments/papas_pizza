from django.db import models
from django.contrib.auth.models import User
from .validators import validate_non_negative, validate_positive


class MenuItem(models.Model):
    """
    Represents an item on a menu, including name,
    description, price, and image.
    """
    name = models.CharField(max_length=55)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_non_negative])
    image = models.ImageField(upload_to='static/images')


    def __str__(self):
        """
        Returns the name of the menu item
        as its string representation.
        """
        return self.name


class Cart(models.Model):
    """
    Represents a shopping cart for a user,
    uniquely linked via one-to-one relationship.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')


    def add_item(self, item, quantity=1):
        """
        Adds a specified quantity of an item to the cart,
        creating or updating the cart item.
        """
        cart_item, created = CartItem.objects.get_or_create(
            item=item, cart=self, 
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
        cart_item.save()


    def remove_item(self, cart_item):
        """
        Removes a specified 
        cart item from the cart.
        """
        cart_item.delete()


    def total_price(self):
        """
        Calculates the total 
        price of all items in the cart.
        """
        return sum(item.subtotal for item in self.items.all())


    def __str__(self):
        """
        Returns a descriptive string indicating
        the owner and number of items in the cart.
        """
        return f"Cart for {self.user.username} with {self.items.count()} items"


