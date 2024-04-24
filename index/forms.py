import logging
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validate_customer_phone_number, validate_customer_street_address, validate_customer_city, validate_customer_zip_code
from .models import PizzaUserProfile

logger = logging.getLogger(__name__)

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

    class Meta:
        """
        Configures PizzaSignUpForm to use the User model and define form fields.
        """
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password1', 'password2',
            'phone_number', 'street_address', 'city', 'zip_code'
        )

    def try_save(self, request, commit=True):
        logger.debug("Attempting to save the user")
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            logger.debug("User saved successfully")
            # Save user profile
            PizzaUserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                street_address=self.cleaned_data['street_address'],
                city=self.cleaned_data['city'],
                zip_code=self.cleaned_data['zip_code']
            )
            logger.debug("User profile saved successfully")
        else:
            logger.debug("Save not committed")
        return user, None

class PasswordResetForm(forms.Form):
    """
    Form for requesting a password reset via email.
    """
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with an optional initial email value.
        """
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.fields['email'].initial = kwargs['initial'].get('email', '')
