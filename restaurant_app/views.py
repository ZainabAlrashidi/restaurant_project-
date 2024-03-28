from django.shortcuts import render,redirect
from .models import MenuItem



def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')

def menu_list(request):
    search_query = request.GET.get('search_name', '')
    meal_type_query = request.GET.get('meal_type', '')

    all_menu_items = MenuItem.objects.all()

    if search_query:
        all_menu_items = all_menu_items.filter(name__icontains=search_query)

    if meal_type_query:
        all_menu_items = all_menu_items.filter(meal_type=meal_type_query)

    context = {'menu_items': all_menu_items}
    return render(request, 'restaurantModule/menu_list.html', context)

def menu_item(request, item_id):
    try:
        targetItem = MenuItem.objects.get(id=item_id)
    except MenuItem.DoesNotExist:
        return redirect('menu_list')
    
    context = {'item': targetItem}
    return render(request, 'restaurantModule/menu_item.html', context)
