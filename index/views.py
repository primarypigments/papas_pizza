from django.shortcuts import render
from .forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from .models import PizzaUserProfile
from menu_cart.models import CartItem, Cart


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
    