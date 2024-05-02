from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.my_signup_view, name='my_signup_view'),
    
    path("accounts/", include('allauth.urls')),

    path('profile/', views.profile, name='profile'),
]

