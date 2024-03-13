from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
     path('menu_items', views.menu_items),
    path('menu_items/<int:item_id>', views.menu_item)
]