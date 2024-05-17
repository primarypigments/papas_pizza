from menu_cart.models import MenuItem


item = MenuItem(
    name='Margherita Pizza',
    description='Classic pizza with mozzarella and tomatoes', price=5.50)
item.save()
