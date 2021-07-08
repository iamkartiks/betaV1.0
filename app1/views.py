from app4.models import *
from app1.models import Institutes
from typing import ContextManager
from django.shortcuts import render
from .models import *

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

def dashboard(request,pk):
    students = Student.objects.get(id=pk)
    careers = students.careeroption_set.all()
    applications = students.application_set.all()
    
    
    context = {'students':students, 'applications':applications,'careers':careers, 'students':students}
    return render(request,'app1/dashboard.html',context)

def institutes(request):
    institutes = Institutes.objects.all()
    context = {'institutes':institutes}
    return render(request,'app1/institutes.html',context)

def course(request):
    course = Course.objects.all()
    context = {'course':course}
    return render(request,'app1/course.html',context)

def complete(request):
    return render(request,'app1/complete.html')