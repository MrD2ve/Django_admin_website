from django import forms
from food.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'}),
        "description": forms.TextInput(attrs={'class': 'form-control'}),
        "category": forms.Select(attrs={'class': 'form-control'}),
        "price": forms.NumberInput(attrs={'class': 'form-control'}),
        "cost": forms.NumberInput(attrs={'class': 'form-control'}),
        "image": forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= "__all__"
        widgets = {
        "first_name":forms.TextInput(attrs={'class':'form-control'}),
        "last_name": forms.TextInput(attrs={'class': 'form-control'}),
        "phone_number": forms.NumberInput(attrs={'class': 'form-control'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= "__all__"
        widgets = {
        "first_name":forms.TextInput(attrs={'class':'form-control'}),
        "last_name":forms.TextInput(attrs={'class':'form-control'}),
        "phone_number": forms.NumberInput(attrs={'class': 'form-control'}),
        "product": forms.Select(attrs={'class': 'form-control'}),
        "status":forms.NumberInput(attrs={'class':'form-control'}),
        }
