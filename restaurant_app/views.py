from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')

def menu_items(request):

    # View to display the menu of the restaurant
    menu_items = [
        {'id': 1, 'name': 'Margherita Pizza', 'description': 'Tomato sauce, mozzarella, and oregano', 'price': 10},
        {'id': 2, 'name': 'Pepperoni Pizza', 'description': 'Pepperoni, tomato sauce, mozzarella', 'price': 12},
        {'id': 3, 'name': 'Bruschetta', 'description': 'Grilled bread garlic, tomatoes, olive oil', 'price': 6},
        # Add more items as needed
    ]
    return render(request, 'restaurantModule/menu_list.html', {'menu_items': menu_items})

def menu_item(request, item_id):
    item1 = {'id': 1, 'name': 'Margherita Pizza', 'description': 'Tomato sauce, mozzarella, and oregano', 'price': 10}
    item2 = {'id': 2, 'name': 'Pepperoni Pizza', 'description': 'Pepperoni, tomato sauce, mozzarella', 'price': 12}
    item3 = {'id': 3, 'name': 'Bruschetta', 'description': 'Grilled bread garlic, tomatoes, olive oil', 'price': 6}
    
    # Find the target menu item based on ID
    targetItem = None
    if item1['id'] == item_id: targetItem = item1
    if item2['id'] == item_id: targetItem = item2
    if item3['id'] == item_id: targetItem = item3

    # Redirect to menu list if item not found
    if targetItem is None: return redirect('menu_list')
    
    # Pass the target item to the template
    context = {'item': targetItem}
    return render(request, 'restaurantModule/menu_item.html', context)