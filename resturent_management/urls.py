from django.urls import path
from . import views
from .views import StockListView,StockCreateView,StockDeleteView,StockDetailView

urlpatterns=[

    path('home',views.homeView,name='home'),
    path('stock/',StockListView.as_view(),name='manage'),
   # path('addItem/',views.addItem,name='addItem'),
    path('add/',StockCreateView.as_view(),name='createStock'),
    path('delete/',StockDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>',StockDetailView.as_view(),name='stock-detail')
    
]