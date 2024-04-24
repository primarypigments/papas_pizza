from django import forms
from .models import CartItem


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

