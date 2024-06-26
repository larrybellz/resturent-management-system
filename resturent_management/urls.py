from django.urls import path

from resturent.views import OrderList
from . import views
from .views import (StockListView,
StockCreateView,StockUpdateView,CategoryListView,
StockDeleteView,StockDetailView,
CategoryCreateView)

urlpatterns=[

    path('home',views.homeView,name='home'),
    path('stock/',StockListView.as_view(),name='stock-list'),
    
   # path('addItem/',views.addItem,name='addItem'),
    path('add/',StockCreateView.as_view(),name='createStock'),
    path('delete/<int:pk>',StockDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>',StockDetailView.as_view(),name='stock-detail'),
    path('<int:pk>/update',StockUpdateView.as_view(),name='update'),
    #categoryurls
    path('category/add',CategoryCreateView.as_view(),name='create-category'),
    path('category/',CategoryListView.as_view(),name='category-list'),
    path('stock-list/category/',views.item_list,name='item-list'),
    
    
]