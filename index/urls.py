from django.urls import path, include
from . import views
from .views import password_reset_request 

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'accounts/password/reset/',
        views.password_reset_request,
        name='account_reset_password'
    ),
    path('accounts/', include('allauth.urls')),


  path(
    'signup/',
    views.my_signup_view,
    name='my_signup_view'
    ),

    path(
        'profile/',
    views.profile,
    name='profile'
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

]
