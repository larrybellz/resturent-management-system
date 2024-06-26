
from turtle import bk
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,User,Group


# Create your models here.

class ClientUser(AbstractUser,PermissionsMixin):
    
    location=models.TextField(max_length=100,blank=True,null=True)
    user_permissions=models.ManyToManyField(User,related_name='client_user_permissions',blank=True)
    groups=models.ManyToManyField(Group,related_name='client_user_groups',blank=True,)

#class StaffUser(AbstractUser,PermissionsMixin):
   
    #location=models.TextField(max_length=100,blank=True,null=True)
    #user_permissions=models.ManyToManyField(ClientUser,related_name='staff_user_permissions',blank=True)
    #groups=models.ManyToManyField(Group,related_name='staff_user_groups',blank=True,)