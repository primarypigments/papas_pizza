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
        max_length=30, required=True, widget=forms.TextInput(attrs={
            'placeholder': _('First name')}), help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(attrs={
            'placeholder': _('Last name')}), help_text='Required.')
    email = forms.EmailField(
        max_length=254, widget=forms.EmailInput(attrs={'placeholder': _(
            'Email')}), help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(
        max_length=15, required=True, validators=[
            validate_customer_phone_number],
        widget=forms.TextInput(attrs={'placeholder': _(
            'Phone number')}), help_text='Optional.')
    street_address = forms.CharField(
        max_length=100, required=True, validators=[
            validate_customer_street_address],
        widget=forms.TextInput(attrs={'placeholder': _('Street address')}))
    city = forms.CharField(
        max_length=50, required=True, validators=[validate_customer_city],
        widget=forms.TextInput(attrs={'placeholder': _('City')}))
    zip_code = forms.CharField(
        max_length=10, required=True, validators=[validate_customer_zip_code],
        widget=forms.TextInput(attrs={'placeholder': _('Zip code')}))
    newsletter_subscribe = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(), help_text=_(
            'Check this box if you want to subscribe to our newsletter.'))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'placeholder': _('Password')}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'placeholder': _(
                'Password confirmation')}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )    

    class Meta:
        """
        Configures PizzaSignUpForm to use the User model and define form fields.
        """
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password1', 'password2',
            'phone_number', 'street_address', 'city', 'zip_code',
            'newsletter_subscribe'
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False  


    def try_save(self, request, commit=True):
        user, _ = super().try_save(request, commit=False)
        if commit:
            user.save()
            PizzaUserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                street_address=self.cleaned_data['street_address'],
                city=self.cleaned_data['city'],
                zip_code=self.cleaned_data['zip_code']
            )
            # Check if user opted for newsletter subscription
            if self.cleaned_data.get('newsletter_subscribe'):
                NewsletterSubscription.objects.create(email=user.email)
            logger.debug("User and profile saved successfully")
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
