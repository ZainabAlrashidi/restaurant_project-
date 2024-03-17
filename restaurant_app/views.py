from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')

def menu_list(request):

    # View to display the menu of the restaurant
    menu_items = [
        {'id': 1, 'name': 'Margherita Pizza', 'description': 'Tomato sauce, mozzarella, and oregano', 'price': 10,'image_url':'https://th.bing.com/th/id/R.93a2878acf479d394d8f4b4b625d39d4?rik=CIVerr9pYI4ovg&pid=ImgRaw&r=0'},
        {'id': 2, 'name': 'Pepperoni Pizza', 'description': 'Pepperoni, tomato sauce, mozzarella', 'price': 12,'image_url':'https://th.bing.com/th/id/R.6bc900c25a3c9fd172764f38acb02e8c?rik=0tpoICbB17axNg&pid=ImgRaw&r=0'},
        {'id': 3, 'name': 'Bruschetta', 'description': 'Grilled bread garlic, tomatoes, olive oil', 'price': 6,'image_url':'https://th.bing.com/th/id/OIP.EqQ-crmMwM0DxxOVNoIDAAHaE8?rs=1&pid=ImgDetMain'},
        # Add more items as needed
    ]
    return render(request, 'restaurantModule/menu_list.html', {'menu_items': menu_items})

def menu_item(request, item_id):
    item1 = {'id': 1, 'name': 'Margherita Pizza', 'description': 'Tomato sauce, mozzarella, and oregano', 'price': 10,'image_url':'https://th.bing.com/th/id/R.93a2878acf479d394d8f4b4b625d39d4?rik=CIVerr9pYI4ovg&pid=ImgRaw&r=0'}
    item2 =  {'id': 2, 'name': 'Pepperoni Pizza', 'description': 'Pepperoni, tomato sauce, mozzarella', 'price': 12,'image_url':'https://th.bing.com/th/id/R.6bc900c25a3c9fd172764f38acb02e8c?rik=0tpoICbB17axNg&pid=ImgRaw&r=0'}
    item3 = {'id': 3, 'name': 'Bruschetta', 'description': 'Grilled bread garlic, tomatoes, olive oil', 'price': 6,'image_url':'https://th.bing.com/th/id/OIP.EqQ-crmMwM0DxxOVNoIDAAHaE8?rs=1&pid=ImgDetMain'}
    
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