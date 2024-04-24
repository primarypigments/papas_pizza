@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()  # Retrieve all cart items
    print(f"Viewing cart for {request.user.username}, Items count: {cart_items.count()}")
    for item in cart_items:
        print(f"Item: {item.item.name}, Quantity: {item.quantity}")
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})
@login_required
def update_item(request, item_id):
    cart = request.user.cart
    form = UpdateCartItemForm(request.POST)
    if form.is_valid():
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        action = form.cleaned_data['action']
        
        if action == 'increment':
            cart_item.quantity += 1  
        elif action == 'decrement':
            cart_item.quantity = max(1, cart_item.quantity - 1)  

        cart_item.save()

    return redirect('cart')

@login_required
@require_POST
def remove_item(request, item_id):
    cart = request.user.cart
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart.remove_item(cart_item)
    return redirect('cart')

@login_required
@require_POST
def checkout(request):
    cart = request.user.cart
    cart.items.clear() 
    cart.save()
    return redirect('order_success') # i still need to work on this


