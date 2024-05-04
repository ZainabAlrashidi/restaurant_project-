from django.shortcuts import render,redirect
from .models import MenuItem
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import MenuItemForm





def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')

def menu_list(request):
    search_query = request.GET.get('search_name', '')
    meal_type_query = request.GET.get('meal_type', '')
    sort_by = request.GET.get('sort', 'name')  # Default sorting by name

    all_menu_items = MenuItem.objects.all()

    if search_query:
        all_menu_items = all_menu_items.filter(name__icontains=search_query)
    if meal_type_query:
        all_menu_items = all_menu_items.filter(meal_type=meal_type_query)

    all_menu_items = all_menu_items.order_by(sort_by)

    context = {'menu_items': all_menu_items}
    return render(request, 'restaurantModule/menu_list.html', context)


def menu_item(request, item_id):
    try:
        targetItem = MenuItem.objects.get(id=item_id)
    except MenuItem.DoesNotExist:
        return redirect('menu_list')
    
    context = {'item': targetItem}
    return render(request, 'restaurantModule/menu_item.html', context)

# views.py


@csrf_exempt
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'restaurantModule/add_menu_item.html', {'form': form})


@csrf_exempt
def edit_menu_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    print(item)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/menu_list')  
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'restaurantModule/edit_menu_item.html', {'form': form})
