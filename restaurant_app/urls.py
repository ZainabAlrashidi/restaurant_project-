from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
     path('menu_list', views.menu_list,name="menu_list"),
    path('menu_item/<int:item_id>', views.menu_item, name='menu_item'),
    path('add_menu_item', views.add_menu_item, name='add_menu_item'),
    path('edit_menu_item/<int:item_id>', views.edit_menu_item, name='edit_menu_item')
]