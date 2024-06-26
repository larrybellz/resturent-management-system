from django.urls import path
from . import views
from .views import DishListView,CategoryListView

urlpatterns=[
    path('',views.index,name='home'),
    path('dishes',views.dishes),
    path('dish/',DishListView.as_view(),name='dish-list'),
    path('categories/',CategoryListView.as_view(),name='client-category-list'),
    path('orders/',views.OrderList,name='order-list'),
   
   
]
