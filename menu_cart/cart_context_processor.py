from decimal import Decimal
from django.contrib.auth.models import User
from .models import Cart, CartItem


def cart_total(request):
    if request.user.is_authenticated:
        cart = request.session.get('cart', {})
        # Convert each stored string subtotal back to Decimal for the calculation
        total = sum(Decimal(item['subtotal']) for item in cart.values())
    else:
        total = 0

    return {'cart_total': total}