from django import forms
from .models import CartItem, MenuItem


class CartAddItemForm(forms.ModelForm):
    """
    A form based on the CartItem model for adding items to a cart.
    Uses the 'quantity' field to specify the number of items to be added.
    """
    class Meta:
        model = CartItem
        fields = ['quantity']

    def clean_quantity(self):
        """
        Ensures that the quantity is a positive integer before saving the form.
        Raises a ValidationError if the quantity is less than or equal to zero.
        """
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive integer")
        return quantity


class UpdateCartItemForm(forms.Form):
    """
    A form for updating the quantity of an item in the cart,
    including performing actions such as
    incrementing or decrementing the quantity.
    """
    quantity = forms.IntegerField(min_value=1)
    action = forms.CharField(max_length=10)

    def clean_quantity(self):
        """
        Validates that the quantity is at least 1.
        Raises a ValidationError if the quantity is less than 1,
        ensuring that there's always at least one item or more.
        """
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1")
        return quantity


class MenuItemForm(forms.ModelForm):
    """
    A form for creating and updating MenuItem objects for the superuser.
    It includes customized input widgets,
    help texts, and labels to improve the user interface in form rendering.

    This form is configured specifically for handling the data of
    menu items such as pizzas,
    including fields for the item's name, description, price, and an image.
    """
    class Meta:
        """
        Meta class for MenuItemForm. Defines the model
        to which the form is linked and
        specifies the model fields to include in the
        form. Additionally, it customizes the
        input widgets, help texts, and labels for a better user experience.
        """
        model = MenuItem
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'name': 'Enter the name of the pizza.',
            'description': 'Enter a brief description of the pizza.',
        }
        labels = {
            'price': 'Price (€)'
        }
