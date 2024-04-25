from django.shortcuts import render,redirect
from .models import MenuItem
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt





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
@csrf_exempt
def add_menu_item(request):
    if request.method == 'POST':
        MenuItem.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            image_url=request.POST['image_url'],
            meal_type=request.POST['meal_type'],
            price=request.POST['price']
        )
        return HttpResponseRedirect('/menu_list')
    return render(request, 'restaurantModule/add_menu_item.html')
@csrf_exempt
def edit_menu_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.image_url = request.POST['image_url']
        item.meal_type = request.POST['meal_type']
        item.price = request.POST['price']
        item.save()
        return HttpResponseRedirect('/menu_list')
    return render(request, 'restaurantModule/edit_menu_item.html', {'item': item})
