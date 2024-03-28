from django.db import migrations

def add_menu_items(apps, schema_editor):
    MenuItem = apps.get_model('restaurant_app', 'MenuItem')
    items_data = [
        {'id': 1, 'name': 'Margherita Pizza', 'description': 'Classic Italian pizza...', 'image_url': 'https://th.bing.com/th/id/R.93a2878acf479d394d8f4b4b625d39d4?rik=CIVerr9pYI4ovg&pid=ImgRaw&r=0', 'meal_type': 'Main Course', 'price': 10},
        {'id': 2, 'name': 'Pepperoni Pizza', 'description': 'Pepperoni, tomato sauce...', 'image_url': 'https://th.bing.com/th/id/R.6bc900c25a3c9fd172764f38acb02e8c?rik=0tpoICbB17axNg&pid=ImgRaw&r=0', 'meal_type': 'Main Course', 'price': 12},
        {'id': 3, 'name': 'Bruschetta', 'description': 'Grilled bread topped...', 'image_url': 'https://th.bing.com/th/id/OIP.EqQ-crmMwM0DxxOVNoIDAAHaE8?rs=1&pid=ImgDetMain', 'meal_type': 'Appetizer', 'price': 6},
        {'id':4, 'name':'Caesar Salad', 'description':'Crispy lettuce with parmesan, croutons, and Caesar dressing', 'image_url':'image_url_for_caesar_salad', 'meal_type':'Starter', 'price':8},
        {'id':5, 'name':'Spaghetti Carbonara', 'description':'Spaghetti pasta with creamy sauce, eggs, Parmesan cheese, and bacon', 'image_url':'image_url_for_spaghetti_carbonara', 'meal_type':'Main Course', 'price':11},
        {'id': 6, 'name': 'Tiramisu', 'description': 'Coffee-flavored Italian dessert...', 'image_url': 'image_url_for_tiramisu', 'meal_type': 'Dessert', 'price': 7}
    ]

    for item in items_data:
        MenuItem.objects.create(**item)

class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_menu_items),
    ]
