from .forms import (
    PasswordResetForm, PizzaSignUpForm, PizzaSignInForm, ContactForm
)
from django.contrib.auth.decorators import login_required
from .models import PizzaUserProfile, ContactMessage
from menu_cart.models import CartItem, Cart
from django.shortcuts import render, redirect, get_object_or_404
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
    Handles password reset requests. If the user is authenticated,
    pre-fills the form with the user's email.
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
    profile = get_object_or_404(PizzaUserProfile, user=request.user)

    carts = Cart.objects.filter(user=request.user)

    template = "profile/profile.html"
    context = {
        "profile": profile,
        # "cart_items": cart_items,
        "carts": carts,
    }
    return render(request, template, context)


def contact(request):
    """
    Handles incoming contact messages or displays the form.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            contact_message.save()

            messages.success(
                request, "Thank you for contacting us!"
                "We will get back to you soon.")
            return redirect('index')
        else:
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def my_signup_view(request):
    """
    Handle user signup, create a user, log events,
    and redirect to index on success. Render signup
    form with errors if invalid.
    """
    if request.method == 'POST':
        form = PizzaSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            logger.info(f"New user signed up: {user.username}")

            if form.cleaned_data.get('newsletter_subscribe'):
                messages.info(
                    request, 'Thank you for signing'
                    ' up for the newsletter!'
                )

            return redirect('index')
        else:
            logger.warning("Signup form validation failed")
            for field, errors in form.errors.items():
                logger.debug(f"{field}: {errors}")
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = PizzaSignUpForm()
    return render(request, 'account/signup.html', {'form': form})
