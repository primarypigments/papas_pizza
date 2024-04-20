from django.db import models
from django.contrib.auth.models import User
from .validators import validate_customer_phone_number, validate_customer_street_address, validate_customer_city, validate_customer_zip_code


class PizzaUserProfile(models.Model):
    """
    Extends User model with contact details and address information.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=17, validators=[validate_customer_phone_number], blank=False)
    street_address = models.CharField(
        max_length=100, validators=[validate_customer_street_address], blank=False)
    city = models.CharField(
        max_length=50, validators=[validate_customer_city], blank=True)
    zip_code = models.CharField(
        max_length=10, validators=[validate_customer_zip_code], blank=True)

    def __str__(self):
        """
    Returns the username associated with the user profile.
        """
        return self.user.username