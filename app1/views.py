from django.shortcuts import render

def index(request):
    return render(request, 'app1/home.html')

def blog(request):
    return render(request,'app1/blog.html')

def login(request):
    return render(request,'app1/login.html')

def register(request):
    return render(request,'app1/register.html')
