from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
     path('menu_list', views.menu_list,name="menu_list"),
    path('menu_item/<int:item_id>', views.menu_item, name='menu_item')
]