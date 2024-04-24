@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()  # Retrieve all cart items
    print(f"Viewing cart for {request.user.username}, Items count: {cart_items.count()}")
    for item in cart_items:
        print(f"Item: {item.item.name}, Quantity: {item.quantity}")
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})

