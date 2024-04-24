from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, CartItem, Cart
from .forms import CartAddItemForm, UpdateCartItemForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def menu_view(request):
    """
    Displays the menu page with all available menu items from the database.
    """
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})


@login_required
def cart_view(request):
    """
    Displays the user's shopping cart page, listing
    all items currently in the cart.
    """
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    print(f"Viewing cart for {request.user.username}, Items count: {cart_items.count()}")
    for item in cart_items:
        print(f"Item: {item.item.name}, Quantity: {item.quantity}")
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})


@login_required
def update_item(request, item_id):
    """
    Updates the quantity of a specific item in the
    user's cart, either incrementing or decrementing it.
    Redirects back to the cart page.
    """
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
    """
    Removes a specified item from the
    user's cart and redirects to the cart page.
    """
    cart = request.user.cart
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart.remove_item(cart_item)
    return redirect('cart')


@login_required
@require_POST
def checkout(request):
    """
    Clears all items from the user's cart upon
    checkout and redirects to a success page.
    """
    cart = request.user.cart
    cart.items.clear()
    cart.save()
    return redirect('order_success') # this is not finished


@login_required
@require_POST
def add_to_cart(request, item_id):
    """
    Adds a specified quantity of an item to the
    user's cart from the menu. Redirects back to the menu.
    """
    print("Adding to cart...")
    item = get_object_or_404(MenuItem, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(
            item=item, cart=cart, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        print(f"Item added: {cart_item.quantity} x {cart_item.item.name} to cart ID {cart.id}")
    else:
        print("Form not valid")
    return redirect('menu')
    