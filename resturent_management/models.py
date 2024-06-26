from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.urls import reverse





class StockItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    description=models.TextField()
    date_updated=models.DateTimeField(default=timezone.now)
 #   category=models.ForeignKey(Category,on_delete=models.CASCADE,default='soup')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})

class Category(models.Model):
    name=models.CharField(max_length=200)
   
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})
    

class Stock(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    description=models.TextField()
    image=models.ImageField(upload_to='dish_image/',null=True,blank=True)
    date_updated=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})

    
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    description=models.TextField()
    image=models.ImageField(upload_to='dish_image/',null=True,blank=True)
    date_updated=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})

    def get_make_order_url(self):
        return reverse('make-order',kwargs={
            'slug':self.slug
        })

    

    



    
