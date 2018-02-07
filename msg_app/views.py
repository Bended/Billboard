# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Messages
from django.views.generic import View
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from datetime import datetime
admin.site.register(Messages)


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# when user connected
def messages(request):
    all_messages = Messages.objects.all()
    context = {
        'all_messages' : all_messages,
        'time':datetime.now(),
        'currentUser': 'Ben',
    }
    return render(request, 'messages.html', context)

#def new_msg():


# check user credential
def bla(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages()
        else:       
            # Return a 'disabled account' error message
            return "disable account"
    else:
        # Return an 'invalid login' error message.
        return "invalide credential"





