from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from authenticate.models import ClientUser,User
from resturent_management.models import MenuItem



# Create your models here.

   



    

class OrderItem(models.Model):
    user=models.ForeignKey(ClientUser,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    menuItem=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.menuItem.name}"

class Order(models.Model):

    user=models.ForeignKey(ClientUser,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
