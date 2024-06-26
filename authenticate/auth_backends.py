from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import ClientUser

class ClientAuthBackend(ModelBackend):
    def authenticate(self, request, username=None , password= None,**kwags):
        try :
            user=ClientUser.objects.get(username=username)
            if user.check_password(password):
                return user
           
        except ClientUser.DoesNotExist:
            return None
    def get_user(self,user_id):
        try:
            return ClientUser.objects.get(pk=user_id)
        except ClientUser.DoesNotExist:
            return None

class StaffAuthBackend(ModelBackend):
    def authenticate(self, request, username=None , password= None, **kwargs):
        try :
            user=User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


