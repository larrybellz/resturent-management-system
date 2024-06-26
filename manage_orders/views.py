from email import message
from django.shortcuts import render,redirect,get_object_or_404
from .models import Order,OrderItem
from resturent_management.models import MenuItem
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def makeOrder(request,pk):
    item =get_object_or_404(MenuItem,pk=pk)
    order_item,created=OrderItem.objects.get_or_create(menuItem=item,
    user=request.user,
    ordered=False)
    #check if they have an order if so then just change the quantity
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(menuItem_id=item.pk).exists():
            order_item.quantity=order_item.quantity+1
            order_item.save()
        else:
            
            order.items.add(order_item)

    else:
            ordered_date=timezone.now()
            order=Order.objects.create(user=request.user,ordered_date=ordered_date)
            order.items.add(order_item)
    messages.info(request,'ordered')
    return redirect('dish-list')

def cancelOrder(request,pk):
    item =get_object_or_404(MenuItem,pk=pk)
   
    return None

 
def confirmOrder(request,pk):
    pendingOrder=orde


    

    