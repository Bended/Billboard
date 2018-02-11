# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Messages
from django.views.generic import View
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime
admin.site.register(Messages)


def home(request):
    return render(request, 'home.html')

def dispLogin(request):
    return render(request, 'login.html')    

@csrf_protect
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect ('messages')
    return redirect ('dispLogin')


def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create_user(username = username, email = email, password = password)
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('messages')

def register_displ(request):
    return render(request, 'register.html')

# when user connected
def messages(request):
    user=request.user
    if user.is_authenticated():
        all_messages = Messages.objects.all()
        context = {
            'all_messages' : all_messages,
            'time':datetime.now(),
        }
        return render(request, 'messages.html', context)
    else:
        return redirect('home')

@csrf_protect
def new_msg(request):
    title = request.POST['title']
    message = request.POST['message']
    author = request.user
    if title is not "" or message is not "":
        new_message = Messages(msg_title = title, msg = message, msg_author = author)
        new_message.save()
        return redirect('messages')
    else:
        return redirect('messages')

@csrf_exempt
def trash(request):
    pkn = request.POST.get("msg_id")
    to_delete = Messages.objects.get(pk = pkn)
    to_delete.delete()
    return HttpResponse("success")
















