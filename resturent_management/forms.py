from dataclasses import fields
from django import forms
from .models import StockItem
class AddItemForm(forms.Form):
    class Meta:
        model=StockItem
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


    #def clean(self):
       #cleaned_data=super().clean()
      # name=cleaned_data.get('name')
       #price=cleaned_data.get('price')
       #description=cleaned_data.get('description')


      # return cleaned_data,name,price,description
