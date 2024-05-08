from django.urls import path
from . import views
from .views import DishListView,CategoryListView

urlpatterns=[
    path('home',views.index,name='home'),
    path('dishes',views.dishes),
    path('dish/',DishListView.as_view(),name='dish-list'),
    path('categories/',CategoryListView.as_view(),name='category-list'),
    path('ordered',views.makeOrder,name='order'),
   
]