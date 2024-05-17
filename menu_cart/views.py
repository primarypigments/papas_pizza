# django imports
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
# custom imports
from .forms import MenuItemForm
from .models import MenuItem, CartItem, Cart, Topping
from .forms import CartAddItemForm, UpdateCartItemForm
from django.core.mail import send_mail 
from decimal import Decimal
import stripe

from django.views.decorators.http import require_POST


import logging

logger = logging.getLogger(__name__)


class SuperUserCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    A mixin that ensures a view can only be
    accessed by superusers. This mixin combines
    LoginRequiredMixin and UserPassesTestMixin
    to first verify that a user is authenticated
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
    cart_total = Decimal('0.00')
    display_items = []

    # Convert cart items into a list suitable for display
    for key, item_details in cart_items.items():
        item_id, *toppings_key = key.split('-')
        item_details['id'] = item_id
        item_details['toppings_key'] = '-'.join(toppings_key) if toppings_key else ''
        
        # Recalculate subtotal to ensure it's always up-to-date
        base_price = Decimal(item_details['price'])
        toppings_total = sum(
            Decimal(topping['price']) for topping in item_details.get(
                'toppings', []))
        item_details[
            'subtotal'] = str((base_price + toppings_total) * item_details[
                'quantity'])
        
        cart_total += Decimal(item_details['subtotal'])
        display_items.append(item_details)
    
    context = {
        'cart_items': display_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart/cart.html', context)

@login_required
def update_item(request, item_id):
    """
    Update the quantity and subtotal of a cart item.
    """
    cart = request.session.get('cart', {})

    form = UpdateCartItemForm(request.POST)
    if form.is_valid():
        action = form.cleaned_data['action']
        item_key = request.POST.get('item_key')

        logger.debug("Attempting to update item with key: %s", item_key)

        if item_key and item_key in cart:
            current_item = cart[item_key]
            if action == 'increment':
                current_item['quantity'] += 1
            elif action == 'decrement':
                current_item['quantity'] = max(1, current_item['quantity'] - 1)

            base_price = Decimal(current_item['price'])
            toppings_total = sum(
                Decimal(topping['price']) for topping in current_item.get(
                    'toppings', []))
            new_subtotal = (base_price + toppings_total) * current_item[
                'quantity']
            current_item['subtotal'] = str(new_subtotal)

            request.session['cart'] = cart
            request.session.modified = True
        else:
            return HttpResponseServerError("Item key not found in cart.")
    else:
        logger.error("Form errors: %s", form.errors)

    return redirect('cart')

@login_required
@require_POST
def remove_item(request, item_id, toppings_key=None):
    """Removes a specified item from the user's session cart."""
    cart = request.session.get('cart', {})

    toppings_key_part = toppings_key if toppings_key else ""
    item_key = f"{
        item_id}-{toppings_key_part}" if toppings_key_part else f"{item_id}-"

    if item_key in cart:
        del cart[item_key]
        request.session['cart'] = cart
        request.session.modified = True
        logger.debug("Removed item %s from cart.", item_key)
        return redirect('cart')
    else:
        logger.error("Item key '%s' not found in cart.", item_key)
        return HttpResponseServerError("Item key not found in cart.")
        
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
@require_POST
def checkout(request):
    """Create a Stripe checkout session and
    redirect to Stripe's payment form."""
    cart_data = request.session.get('cart', {})
    cart_total = Decimal('0.00')

    if cart_data:
        with transaction.atomic():
            # Check if the user already has a cart
            new_cart = Cart.objects.create(
                user=request.user
            )
            items_for_stripe = []

            for cart_key, item_details in cart_data.items():
                item_id, toppings_key = (cart_key.split('-', 1) + [""])[:2]
                item = MenuItem.objects.get(id=item_id)
                quantity = int(item_details['quantity'])
                price_per_item = Decimal(item_details['subtotal']) / quantity  

                cart_item = CartItem.objects.create(
                    cart=new_cart,
                    item=item,
                    quantity=quantity,
                    subtotal=item_details['subtotal']
                )
                toppings = Topping.objects.filter(
                    id__in=(toppings_key.split('-') if toppings_key else []))
                cart_item.toppings.set(toppings)

                items_for_stripe.append({
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {'name': item.name},
                        'unit_amount': int(price_per_item * 100)
                    },
                    'quantity': quantity
                })

            if items_for_stripe:
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=items_for_stripe,
                    mode='payment',
                    success_url=request.build_absolute_uri(
                        reverse('checkout_success', kwargs={
                            'cart_id': new_cart.id})),
                    cancel_url=request.build_absolute_uri('/cancel/')
                )
                request.session['cart'] = {}  # Clear the cart
                return redirect(session.url)

@login_required
def checkout_success(request, cart_id):
    """
    Handle successful checkout and send confirmation email.
    """
    try:
        cart = Cart.objects.get(id=cart_id, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total = sum(item.subtotal for item in cart_items)

        # Check if the email has already been sent
        if not request.session.get(f'email_sent_{cart_id}', False):
            send_mail(
                "Pappa's Pizza Order Confirmation",
                f"Your order has been placed successfully.\n\n"
                f"Order Total: €{total}\n"
                f"Order Date: {cart.created_at}\n\n"
                "Thank you, from Pappa's Pizza!",
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            # Set the email sent flag in the session
            request.session[f'email_sent_{cart_id}'] = True

        return render(
            request, 'checkout/success.html', {'cart': cart, 'total': total})
        
    except Cart.DoesNotExist:
        return HttpResponseNotFound("Cart not found.")
    except Exception as e:
        return render(request, 'checkout/error.html', {'message': str(e)})


def checkout_success_profile(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total = sum(item.subtotal for item in cart_items)

        return render(
            request, 'checkout/success_profile.html', {
                'cart': cart, 'total': total})
        
    except Cart.DoesNotExist:
        return HttpResponseNotFound("Cart not found.")
    except Exception as e:
        return render(request, 'checkout/error.html')


def error_view(request):
    
    return render(request, 'checkout/error.html')


def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})

    form = CartAddItemForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        selected_toppings = request.POST.getlist('toppings')

        # Sorting toppings to create a consistent key, always include a dash
        sorted_toppings = sorted(int(tid) for tid in selected_toppings)
        toppings_key = "-".join(
            map(str, sorted_toppings)) if sorted_toppings else ""
        cart_key = f"{
            item_id}-{toppings_key}" if toppings_key else f"{item_id}-"

        # Initialize or update cart item data
        if cart_key in cart:
            cart_item = cart[cart_key]
            cart_item['quantity'] += quantity
            new_subtotal = Decimal(
                cart_item['subtotal']) + (Decimal(item.price) + Decimal(sum(
                    Topping.objects.filter(
                        id__in=sorted_toppings).values_list(
                            'price', flat=True))) * quantity)
            cart_item['subtotal'] = str(new_subtotal)
        else:
            # Calculate total price for toppings
            toppings = Topping.objects.filter(id__in=sorted_toppings)
            topping_details = [{'name': topping.name, 'price': str(
                topping.price)} for topping in toppings]
            toppings_total = sum(
                Decimal(topping.price) for topping in toppings) * quantity

            # New cart item
            cart[cart_key] = {
                'quantity': quantity,
                'price': str(item.price),
                'name': item.name,
                'subtotal': str(
                    Decimal(item.price) * quantity + toppings_total),
                'image_url': item.image.url if item.image else None,
                'toppings': topping_details
            }

        # Update session
        request.session['cart'] = cart
        request.session.modified = True

    return redirect('menu')

def menu_view(request):
    """
    View function for displaying the menu page and
    processing item additions or updates.
    It handles both GET and POST requests: GET requests render
    the menu page with available
    items and an item form, while POST requests handle the
    addition or updating of menu items.
    """
    logger.info("Entering menu_view function")

    if request.method == 'POST':
        item_form = MenuItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            logger.info("Form is valid. Saving new item.")
            item_form.save()
            return redirect('menu')
        else:
            logger.warning("Form is invalid.")
            logger.warning(item_form.errors)  # Log form errors
            return render(request, 'menu/menu.html', {
                'menu_items': MenuItem.objects.all(),
                'item_form': item_form,
                'toppings': Topping.objects.all(),
                'form_errors': item_form.errors
            })
    else:
        logger.info("Rendering menu page")
        menu_items = MenuItem.objects.all()
        item_form = MenuItemForm()
        context = {
            'menu_items': menu_items,
            'item_form': item_form,
            'toppings': Topping.objects.all(),
        }
        return render(request, 'menu/menu.html', context)

    logger.error("No valid conditions met. Redirecting to menu page.")
    return redirect('menu')

@login_required
def edit_menu_item(request, item_id):
    """
    View function for editing an existing
    menu item. This function is accessible
    only by superusers. It handles the
    retrieval and updating of a MenuItem object.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access denied. Invalid credentials.")
        return redirect('menu')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == "POST":
        item_form = MenuItemForm(
            request.POST or None, request.FILES, instance=menu_item)
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
    View function for deleting a specific
    MenuItem identified by item_id. This function
    is restricted to superusers only,
    ensuring secure management of menu items.
    """
    if not request.user.is_superuser:
        messages.error(request, "Access denied. Invalid credentials.")
        return redirect('menu')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    menu_item.delete()
    messages.success(request, "Menu Item deleted!")
    return redirect('menu')
