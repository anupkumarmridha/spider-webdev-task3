from dataclasses import fields
from django import forms
from home.models import Product,Category, Comment

choices=Category.objects.all().values_list('name','name')
choices_list=[]
for cats_item in choices:
    choices_list.append(cats_item)



class PostProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('title', 'title_tag','category', 'author', 'desc','product_image', 'price')
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'category': forms.Select(choices=choices_list ,attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user_id', 'type':'hidden'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('title', 'title_tag', 'category', 'desc', 'product_image', 'price')
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'category': forms.Select(choices=choices_list ,attrs={'class': 'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }
        
        