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


