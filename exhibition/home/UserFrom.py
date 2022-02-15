from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from home.models import Profile

class EditProfileFrom(UserChangeForm):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model=User
        fields =('username', 'first_name', 'last_name', 'email', 'password')

class AddProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio', 'website_url','facebook_url', 'twitter_url', 'instagram_url','profile_pic')
        widgets={
            'bio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title Tag'}),
            'user': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user_id', 'type':'hidden'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your Old Password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter New Password'}))
    new_password2=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm New Password'}))
    class Meta:
        model=User
        fields =('old_password', 'new_password1', 'new_password2')

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [] 
