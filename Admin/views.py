from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import ContactForm,RegisterUserForm,PasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
# Create your views here.
import requests,secrets,random
import datetime,time
from .models import AdminContact

def LoginAdmin(request):
    if request.method=="POST":
        user_email=request.POST['email']
        password=request.POST['password']
        try:
            usernames = User.objects.get(email=user_email)
            user=authenticate(request,username=usernames.username,password=password)
            if user is not None :
                login(request,user)
                return redirect('dashboard')
            else:
                #.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
                return redirect('Adminlogin')
        except User.DoesNotExist:
            pass
    else:
        return render(request,'login.html',{})


def log_outAdmin(request):
    logout(request)
    return redirect('Adminlogin')