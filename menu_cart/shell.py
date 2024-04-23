from menu_cart.models import MenuItem

# Create a new menu item instance
item = MenuItem(name='Margherita Pizza', description='Classic pizza with mozzarella and tomatoes', price=5.50)
item.save()  # Save the item to the database

# Add an image if your model requires it, you'll need to handle image files properly