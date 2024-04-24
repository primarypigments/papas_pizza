from django.urls import path
from . import views

urlpatterns = [
    path('update-item/<int:item_id>/', views.update_item, name='update_item'),
    path('remove-item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('menu/', views.menu_view, name='menu'),
    path('cart/', views.cart_view, name='cart'),
]