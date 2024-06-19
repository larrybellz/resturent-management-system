from ast import Return
from multiprocessing import context
from .models import Order,Client
from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from django.db import models
from resturent_management.models import Stock,Category

# Create your views here.
def index(request):
    return render(request,'resturent/index.html')

def dishes(request):
    return render(request,'resturent/dishes.html')


class DishListView(ListView):
    paginate_by=4
    
    model=Stock
    template_name='resturent/dishes.html'
    context_object_name='dishes'
    ordering=['-pk']
   
class CategoryListView(ListView):
    paginate_by=4
    
    model=Category
    template_name='resturent/categories.html'
    context_object_name='categories'
    ordering=['-pk']
def makeOrder(request,pk):

    
    if request.method=='POST':
        myorder=Order()
        selected_dish=Stock.objects.get(id=id)
        myorder.dish_name=selected_dish.kj
        print('JUST ORDERED')

    return redirect('dish-list')


    