from ast import Return
from multiprocessing import context
import re
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from manage_orders.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from resturent_management.models import Stock,Category,MenuItem

# Create your views here.
def index(request):
    return render(request,'resturent/index.html')

def dishes(request):
    return render(request,'resturent/dishes.html')


class DishListView(ListView):
    paginate_by=4
    
    model=MenuItem
    template_name='resturent/dishes.html'
    context_object_name='dishes'
    ordering=['-pk']
   
class CategoryListView(ListView):
    paginate_by=4
    
    model=Category
    template_name='resturent/categories.html'
    context_object_name='categories'
    ordering=['-pk']

def OrderList(request):
    try:
        order=Order.objects.get(user=request.user,ordered=False)
        context={
            'orders':order
        }
        return render(request,'resturent/orders.html',context)
    except ObjectDoesNotExist:
        messages.error(request,'you do not have active orders')
        return redirect('/')
 