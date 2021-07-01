from typing import ContextManager
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'app1/home.html', context)

def blog(request):
    context = {}
    return render(request,'app1/blog.html', context)

def login(request):
    context ={}
    return render(request,'app1/login.html', context)

def register(request):
    context = {}
    return render(request,'app1/register.html', context)

def dashboard(request):
    context = {}
    return render(request,'app1/dashboard.html')
