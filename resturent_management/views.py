from email import message
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render,redirect
from .models import StockItem,Category,Stock
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from .forms import AddItemForm,UpdateForm
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.
def homeView(request):
    return render(request,'resturent_management/manage_products.html')

class StockListView(ListView):
    model=Stock
    template_name='resturent_management/manage_products.html'
    context_object_name='items'
    ordering=['-pk']
    queryset= Stock.objects.all()

    
  #  def get_queryset(self):
   #     stocks=self.queryset
     #   categories=Category.objects.all()
       
    #    return list(zip(stocks,categories)),

    

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()#add categories to the context
        return context
    



    
def item_list(request):
    selected_category_id=request.GET.get('category')
    if selected_category_id:
        items=Stock.objects.filter(category_id=selected_category_id)
        


    else:#to show all items if selected view all items
        items=Stock.objects.all()
    context={
        'items':items,
        'categories':Category.objects.all()

    }
    return render(request,'resturent_management/manage_products.html',context)




class StockCreateView(CreateView):
    model=Stock
    template_name='resturent_management/additem.html'
    form=AddItemForm
    fields=['name','price','description','category']
    success_url='/stock/'
    
    def get_success_message(self,request):
        messages.add_message(request,)
   
   

    

    def form_valid(self,form ):
        messages.add_message(self.request,messages.SUCCESS,'stock created')
        return super().form_valid(form)
        

class StockDeleteView(DeleteView):
    model=Stock
    success_url='/stock/'
    context_object_name='item'
    template_name='resturent_management/deleteConfirm.html'


       
        

class StockDetailView(DetailView):
    model=Stock
    context_object_name='item'
    success_url='/stock/'
    template_name='resturent_management/stock_detail.html'
    
class StockUpdateView(UpdateView):
    model=Stock
    template_name='resturent_management/update.html'
    form=UpdateForm
    fields=['name','price','description','category']
    success_url='/stock/'

   

class CategoryListView(ListView):
    model=Category
    template_name='resturent_management/categoryList.html'
    context_object_name='categories'
    ordering=['-pk']

    
    def get_queryset(self):
        return Category.objects.all()

class CategoryCreateView(CreateView):
    model=Category
    template_name='resturent_management/addcategory.html'
    form=AddItemForm
    fields=['name','description']
    success_url='/category/'
    
    def get_success_message(self,request):
        messages.add_message(request,)
   
   

    

    def form_valid(self,form ):
        messages.add_message(self.request,messages.SUCCESS,'category  created succesfully')
        return super().form_valid(form)
        








