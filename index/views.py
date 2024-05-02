from .forms import PasswordResetForm, PizzaSignUpForm, PizzaSignInForm
from django.contrib.auth.decorators import login_required
from .models import PizzaUserProfile
from menu_cart.models import CartItem, Cart
from django.shortcuts import render, redirect
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)

def index(request):
    """
    Renders the main page of the site using the 'index/index.html' template.
    It provides an empty context dictionary for potential future use.
    """
    template = "index/index.html"
    context = {}
    return render(request, template, context)


def password_reset_request(request):
    """
    Handles password reset requests. If the user is authenticated, pre-fills the form with the user's email.
    Processes the form submission if method is POST and the form is valid.
    """
    if request.user.is_authenticated:
        initial_data = {
            'email': request.user.email
        }
        form = PasswordResetForm(initial=initial_data)
    else:
        form = PasswordResetForm()

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Process the form
            pass

    return render(request, 'your_template_name.html', {'form': form})


@login_required
def profile(request):
    """
    Displays the user's profile with related information.
    """
    profiles = PizzaUserProfile.objects.filter(user=request.user)

    try:
        user_cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=user_cart)
    except Cart.DoesNotExist:
        cart_items = []

    template = "profile/profile.html"
    context = {
        "profiles": profiles,
        "cart_items": cart_items
    }
    return render(request, template, context)
    

def my_signup_view(request):
    if request.method == 'POST':
        form = PizzaSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            logger.info(f"New user signed up: {user.username}")

            if form.cleaned_data.get('newsletter_subscribe'):
                messages.info(request, 'Thank you for signing' 
                'up for the newsletter!')

            return redirect('index')
        else:
            logger.warning("Signup form validation failed")
            for field, errors in form.errors.items():
                logger.debug(f"{field}: {errors}")
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = PizzaSignUpForm()
    return render(request, 'account/signup.html', {'form': form})
    