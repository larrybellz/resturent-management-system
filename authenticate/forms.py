from dataclasses import fields
from django import forms
from .models import ClientUser
class ClientRegistrationForm(forms.Form):
    class Meta:
        model=ClientUser
        fields=['username','email','password','confirm_password','location']