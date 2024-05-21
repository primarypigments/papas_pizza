from django.urls import path
from . import views
from .views import error_view


urlpatterns = [

    path(
        'update-item/<int:item_id>/',
        views.update_item,
        name='update_item'
    ),

    path(
        'remove-item/<int:item_id>/',
        views.remove_item,
        name='remove_item'
    ),

    path(
        'remove-item/<int:item_id>/<str:toppings_key>/',
        views.remove_item,
        name='remove_item_with_toppings'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'checkout/success/<int:cart_id>/',
        views.checkout_success,
        name='checkout_success'
    ),
    path('error/', views.error_view, name='checkout_error'),

    path(
        'checkout/success_profile/<int:cart_id>/',
        views.checkout_success_profile,
        name='checkout_success_profile'
    ),

    path(
        'add-to-cart/<int:item_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'menu/',
        views.menu_view,
        name='menu'
    ),

    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'edit_menu_item/<int:item_id>/',
        views.edit_menu_item, name='edit_menu_item'
    ),

    path(
        'delete_menu_item/<int:item_id>/',
        views.delete_menu_item,
        name='delete_menu_item'
    ),

]
