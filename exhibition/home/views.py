from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView 
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views import generic
from home.models import Product,Category,Profile
from home.UserFrom import EditProfileFrom, UserPasswordChangeForm, AddProfileForm




#import re
from home.EmailBackEnd import EmailBackEnd

# Create your views here.
class homeView(ListView):
    model=Product
    template_name='home/home.html'
    ordering=['-created_at']
    
    def get_context_data(self, *args,**kwargs):
        cats_menu=Category.objects.all()
        context=super(homeView, self).get_context_data(*args, **kwargs)
        context['cats_menu']=cats_menu
        return context

class UserProfileView(DetailView):
    model=User
    template_name='user/view_profile.html'


class AddProfileDetailsView(CreateView):
    model=Profile
    form_class=AddProfileForm
    template_name='user/add_ProfileDetails.html'

    def get_success_url(self):
        return reverse_lazy('View_Profile',kwargs={'pk': self.object.pk})
    
    def get_object(self):
        return self.request.user


class UserEditView(generic.UpdateView):
    form_class=EditProfileFrom
    template_name='user/edit_profile.html'
    success_url=reverse_lazy('homeView')

    def get_object(self):
        return self.request.user

class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name='user/password_change.html'
    success_url=reverse_lazy('homeView')

def handleLogin(request):
    if request.method != 'POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfuly logged in 🥰")
            return redirect('homeView')
        else:
            messages.error(request,"Invalid credentials, please try again 😎")
            return redirect('homeView')
    
    
def handleLogout(request):
    if request.method=='POST':
        value=request.POST['value']
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")
        return redirect('homeView')
    else:
        return HttpResponse('Sorry No Users Logged in 😎')   
 
def handelSingup(request):
    if request.method =='POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user_exist = User.objects.filter(username=username).exists()
        email_exist = User.objects.filter(email=email).exists()
        if email_exist:
            messages.error(request, "Email Exist!!")
            return redirect('homeView')
        #check for errorneous input
        #username
        else:
            if len(username) > 25:
                messages.error(request, "username is too long(must be less than 26 character)")
                return redirect('homeView')
            if len(username) < 3:
                messages.error(request, "'username is short(must be more than 2 character)")
                return redirect('homeView')
                #password
            if len(pass1) < 8:
                messages.error(request, "Make sure your password is at lest 8 characters")
                return redirect('homeView')
            if len(pass1) > 20:
                messages.error(request, "Make sure your password is under 20 characters")
                return redirect('homeView')
                #pass1 & pass2 should be same
            if pass1 != pass2 :
                messages.error(request, "Password do not match.")
                return redirect('homeView')
            #Create User
            try:
                myuser = User.objects.create_user(username=username, email=email,password=pass1)
                myuser.first_name=fname
                myuser.last_name=lname
                myuser.save()
                messages.success(request, "your account has been successfully created 🥰")
                return redirect('homeView')
            except:
                if user_exist:
                    messages.error(request, "username Exits")
                messages.error(request, "Failed to SignUp!")
                return redirect('homeView')


class UserEditView(generic.UpdateView):
    form_class=EditProfileFrom
    template_name='user/edit_profile.html'
    
    def get_success_url(self):
        return reverse_lazy('View_Profile',kwargs={'pk': self.object.pk})

    def get_object(self):
        return self.request.user

"""
class DeleteUserProfileView(LoginRequiredMixin,DeleteView):
    model=User
    template_name='user/delete_account.html'    

    def get_object(self, queryset=None):
        if request.method == 'POST':
            delete_form = UserDeleteForm(request.POST, instance=request.user)
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('homeView')
        else:
            delete_form = UserDeleteForm(instance=request.user)
    
"""

