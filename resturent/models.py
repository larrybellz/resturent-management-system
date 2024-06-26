from platform import mac_ver
from posixpath import basename
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


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


   
