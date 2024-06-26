from django.urls import path
from . import views

urlpatterns=[
    path('make-order/<int:pk>/',views.makeOrder,name='make-order')
]