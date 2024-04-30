# django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# custom imports
from .forms import MenuItemForm
from .models import MenuItem, CartItem, Cart, Topping
from .forms import CartAddItemForm, UpdateCartItemForm

import logging


class SuperUserCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
      A mixin that ensures a view can only be accessed by superusers. This mixin combines
    LoginRequiredMixin and UserPassesTestMixin to first verify that a user is authenticated
    and then checks if the user is a superuser.
    """
    def test_func(self):
        """
        Determine if the currently authenticated user is a superuser.
        """
        return self.request.user.is_superuser


@login_required
def cart_view(request):
    """ Display the user's shopping cart from session. """
    cart_items = request.session.get('cart', {})
    # Ensure conversion of subtotal from string to Decimal before summing
    cart_total = sum(Decimal(item['subtotal']) for item in cart_items.values())

    context = {
        'cart_items': cart_items.items(),  # Pass items as (id, details)
        'cart_total': cart_total,
    }
    return render(request, 'cart/cart.html', context)

@login_required
@require_POST
def update_item(request, item_id):
    """Updates the quantity of a specific item in the user's session cart."""
    cart = request.session.get('cart', {})
    form = UpdateCartItemForm(request.POST)
    if form.is_valid():
        action = form.cleaned_data['action']
        if item_id in cart:
            if action == 'increment':
                cart[str(item_id)]['quantity'] += 1
            elif action == 'decrement':
                cart[str(item_id)]['quantity'] = max(1, cart[str(item_id)]['quantity'] - 1)

            # Update session
            request.session['cart'] = cart

    return redirect('cart')


@login_required
@require_POST
def remove_item(request, item_id):
    """Removes a specified item from the user's session cart."""
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]

        # Update session
        request.session['cart'] = cart

    return redirect('cart')


@login_required
@require_POST
def checkout(request):
    """ Transfers session cart to database 
    upon checkout and clears the session. 
    """
    cart_data = request.session.get('cart', {})
    
    if cart_data:
        with transaction.atomic():
            new_cart = Cart.objects.create(user=request.user)
            for item_id, item_details in cart_data.items():
                item = MenuItem.objects.get(id=item_id)
                cart_item = CartItem.objects.create(
                    cart=new_cart,
                    item=item,
                    quantity=item_details['quantity'],
                    subtotal=item_details['subtotal']
                )
                # Assume toppings are stored in session with their IDs
                toppings = Topping.objects.filter(id__in=item_details.get('toppings', []))
                cart_item.toppings.set(toppings)
            
            # Optionally clear the session cart
            del request.session['cart']
            new_cart.save()
        return redirect('order_success')
    

@login_required
@require_POST
def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})

    # Initialize cart item data
    cart_item = cart.get(str(item_id), {
        'quantity': 0,
        'price': str(item.price),
        'name': item.name,
        'subtotal': '0.00',
        'image_url': item.image.url if item.image else None,
        'toppings': []
    })

    form = CartAddItemForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        selected_toppings = request.POST.getlist('toppings')

        # Retrieve toppings and calculate their total price
        toppings = Topping.objects.filter(id__in=selected_toppings)
        topping_details = [{'name': topping.name, 'price': str(topping.price)} for topping in toppings]
        toppings_total = sum(Decimal(topping.price) for topping in toppings) * quantity

        # Update quantity and subtotal
        cart_item['quantity'] += quantity
        cart_item['toppings'].extend(topping_details)  # Add topping details for display
        current_subtotal = Decimal(cart_item['subtotal']) + (Decimal(cart_item['price']) * quantity) + toppings_total
        cart_item['subtotal'] = str(current_subtotal)

        # Update session
        cart[str(item_id)] = cart_item
        request.session['cart'] = cart

    return redirect('menu')


def menu_view(request):
    """
    View function for displaying the menu page and processing item additions or updates.
    It handles both GET and POST requests: GET requests render the menu page with available
    items and an item form, while POST requests handle the addition or updating of menu items.
    """
    logger = logging.getLogger(__name__)
    logger.info("Entering menu_view function")
    
    if request.method == 'POST':
        logger.info("Processing POST request")
        
        if 'add_item' in request.POST:
            logger.info("Add item form submitted")
            
            item_form = MenuItemForm(request.POST, request.FILES)
            if item_form.is_valid():
                logger.info("Form is valid. Saving new item.")
                
                item_form.save()
                return redirect('menu')
            else:
                logger.warning("Form is invalid.")
                logger.warning(item_form.errors)  # Log form errors
        else:
            item_id = request.POST.get('item_id')
            item = MenuItem.objects.get(pk=item_id)
            item_form = MenuItemForm(request.POST, request.FILES, instance=item)
            if item_form.is_valid():
                logger.info("Form is valid. Saving edited item.")
                
                item_form.save()
                return redirect('menu')
            else:
                logger.warning("Form is invalid.")
                logger.warning(item_form.errors)  # Log form errors
    else:
        logger.info("Rendering menu page")
        
        menu_items = MenuItem.objects.all()
        item_form = MenuItemForm()
        template = 'menu/menu.html'
        context = {
            'menu_items': menu_items,
            'item_form': item_form,
            'toppings': Topping.objects.all(),
        }
        return render(request, template, context)
    
    # In case none of the conditions are met, log an error and return a redirect to the menu page
    logger.error("No valid conditions met. Redirecting to menu page.")
    return redirect('menu')


@login_required
def edit_menu_item(request, item_id):
    """
    View function for editing an existing menu item. This function is accessible
    only by superusers. It handles the retrieval and updating of a MenuItem object.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access denied. Invalid credentials.")
        return redirect('menu')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == "POST":
        item_form = MenuItemForm(request.POST or None, request.FILES, instance=menu_item)
        if item_form.is_valid():
            item_form.save()
            messages.success(request, "Menu Item updated!")
            return redirect('menu')
        messages.error(request, "Error, please try again!")

    item_form = MenuItemForm(instance=menu_item)
    template = 'menu/edit_menu_item.html'
    context = {
        'menu_item': menu_item,
        'item_form': item_form,
    }
    return render(request, template, context)


@login_required
def delete_menu_item(request, item_id):
    """
    View function for deleting a specific MenuItem identified by item_id. This function
    is restricted to superusers only, ensuring secure management of menu items.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access denied. Invalid credentials.")
        return redirect('menu')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    menu_item.delete()
    messages.success(request, "Menu Item deleted!")
    return redirect('menu')
