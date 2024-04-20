from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validate_customer_phone_number, validate_customer_street_address, validate_customer_city, validate_customer_zip_code

class PizzaSignUpForm(UserCreationForm):
    """
    Form for user signup with personal 
    info and address, extending UserCreationForm.
    """
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(
        max_length=15, required=True, validators=[
            validate_customer_phone_number], help_text='Optional.')
    street_address = forms.CharField(
        max_length=100, required=True, validators=[
            validate_customer_street_address])
    city = forms.CharField(
        max_length=50, required=True, validators=[
            validate_customer_city])
    zip_code = forms.CharField(
        max_length=10, required=True, validators=[
            validate_customer_zip_code])
