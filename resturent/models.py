from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.urls import reverse


# Create your models here.
#model that creates a unique id
class UUIDField(models.CharField):
    def __init__(self,*args,**kwargs):
        kwargs['max_length']=6
        super(UUIDField,self).__init__(*args,**kwargs)
    def pre_save(self,model_instance,add):
        if add:
            letters='abcdefghijklmnopqrstuvwxyz'
            first_digit=get_random_string(1,letters)
            middle_digit=get_random_string(4,'123456789')
            last_digit=get_random_string(1,letters)

            value=f'{first_digit}{middle_digit}{last_digit}'

            return value

        return super(UUIDField,self.pre_save(model_instance,add))



class Order(models.Model):
    #order_id=UUIDField(primary_key=True,editable=False)
    dish_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    
    order_date=models.DateTimeField(default=timezone.now)
    order_state=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.dish_name

    def get_absolute_url(self):
        return reverse('stock-detail',kwargs={'pk':self.pk})
