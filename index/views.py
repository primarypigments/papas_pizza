from django.shortcuts import render
from .forms import PasswordResetForm


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