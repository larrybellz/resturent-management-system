from dataclasses import fields
from django import forms
from .models import Stock,MenuItem
class AddItemForm(forms.Form):
    class Meta:
        model=MenuItem
        fields=['name','price','description','image']
    name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Item name',
        'class':'itemName ',
       

    }
    ))
    price=forms.DecimalField(widget=forms.NumberInput(attrs={
       'name':'price',
   }))
    description=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Item name',
 
    }
    ))

class UpdateForm(forms.Form):
    class Meta:
        model=MenuItem
        fields=['name','price','description']

    name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Item name',
       'class':'itemName',
       

    }
    ))
    price=forms.DecimalField(widget=forms.NumberInput(attrs={
        'name':'price'
    }))
    description=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Item name',
 
    }
    ))


