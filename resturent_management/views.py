from msilib.schema import ListView
from pyexpat import model
from re import template
from django.shortcuts import render,redirect
from .models import StockItem
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from .forms import AddItemForm
from django.views.generic.edit import CreateView

# Create your views here.
def homeView(request):
    return render(request,'resturent_management/manage_products.html')

class StockListView(ListView):
    model=StockItem
    template_name='resturent_management/manage_products.html'
    context_object_name='items'
    ordering=['-pk']

    
    def get_queryset(self):
        return StockItem.objects.all()

class StockCreateView(CreateView):
    model=StockItem
    template_name='resturent_management/additem.html'
    form=AddItemForm
    fields=['name','price','description']
    success_url='/stock/'
   

    

    def form_valid(self,form ):
        return super().form_valid(form)

class StockDeleteView(DeleteView):
    model=StockItem
    success_url='/stock/'
    template_name='resturent_management/deleteConfirm.html'

class StockDetailView(DetailView):
    model=StockItem
    context_object_name='item'
    success_url='/stock/'
    template_name='resturent_management/stock_detail.html'







"""def addItem(request):
    form=AddItemForm(request.POST)
   
    context={
        'form':form,
        
    }
    #get form data
    
    

    if request.method=="POST":
        if form.is_valid:
            StockItem.objects.create(
               
                description=form.cleaned_data['decription'],
                price=form.cleaned_data['price']
            )





        return redirect('manage/')
            
 
    else:
         return render(request,'resturent_management/addItem.html',context)

            


  
    return render(request,'resturent_management/addItem.html',context)"""

'''class addItemView(CreateView):
    
    model=StockItem
    form=AddItemForm
    template_name='resturent_management/addItem.html'
    success_url='manage/'
    def form_valid(self,form):
        
        return super().form_valid(form)'''



