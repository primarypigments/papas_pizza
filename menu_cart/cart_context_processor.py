from django.contrib.auth.models import User
from .models import Cart, CartItem


def cart_total(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        total = cart.total_price()
    else:
        total = 0

    return {'cart_total': total}
