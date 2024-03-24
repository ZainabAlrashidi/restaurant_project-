from django.shortcuts import render,redirect

# Create your views here.
def __getMenuItems():
    return [
        {
            'id': 1,
            'name': 'Margherita Pizza',
            'description': 'Classic Italian pizza with tomato sauce, mozzarella, and basil',
            'image_url': 'https://th.bing.com/th/id/R.93a2878acf479d394d8f4b4b625d39d4?rik=CIVerr9pYI4ovg&pid=ImgRaw&r=0',
            'meal_type': 'Main Course',
            'price':10
        },
        {
            'id': 2,
            'name': 'Pepperoni Pizza',
            'description': 'Pepperoni, tomato sauce, and mozzarella on a golden crust',
            'image_url': 'https://th.bing.com/th/id/R.6bc900c25a3c9fd172764f38acb02e8c?rik=0tpoICbB17axNg&pid=ImgRaw&r=0',
            'meal_type': 'Main Course',
            'price':12
        },
        {
            'id': 3,
            'name': 'Bruschetta',
            'description': 'Grilled bread topped with garlic, fresh tomatoes, olive oil, and basil',
            'image_url': 'https://th.bing.com/th/id/OIP.EqQ-crmMwM0DxxOVNoIDAAHaE8?rs=1&pid=ImgDetMain',
            'meal_type': 'Appetizer',
            'price':6
        }
    ]


def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')

def menu_list(request):
    all_menu_items = __getMenuItems()
    search_query = request.GET.get('search_name', '')
    meal_type_query = request.GET.get('meal_type', '')

    if search_query:
        all_menu_items = [item for item in all_menu_items if search_query.lower() in item['name'].lower()]

    if meal_type_query:
        all_menu_items = [item for item in all_menu_items if item['meal_type'] == meal_type_query]

    context = {'menu_items': all_menu_items}
    return render(request, 'restaurantModule/menu_list.html', context)


def menu_item(request, item_id):
    menu_items = __getMenuItems()
    targetItem = next((item for item in menu_items if item['id'] == item_id), None)

    if targetItem is None:
        return redirect('menu_list')
    
    context = {'item': targetItem}
    return render(request, 'restaurantModule/menu_item.html', context)
