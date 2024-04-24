class CartAddItemForm(forms.ModelForm):
    """
    A form based on the CartItem model for adding items to a cart.
    Uses the 'quantity' field to specify the number of items to be added.
    """
    class Meta:
        model = CartItem
        fields = ['quantity']

