from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages

from list_of_request.models import Articles
from .forms import LoginUserForm



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            
            return redirect('userprofile:login')
    else:
        form = UserCreationForm(request.POST)
        
    return render(request, 'userprofile/signup.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('list_of_request:applications'))
    else:
        form = LoginUserForm()
    return render(request, 'userprofile/login.html', {'form': form})
            

        
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('userprofile:login'))
            
            
        
        