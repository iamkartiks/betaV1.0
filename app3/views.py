from django.shortcuts import render
from .models import *
from app1.models import *
from app4.models import *

def managementsys(request):
    
    return render(request, 'app3/managementsys.html')

def dashboard(request, pk):
    
    institute = Institutes.objects.get(id=pk)
    
    events = Event.objects.filter(institute=institute)
    
    registered_students = Registered.objects.filter(institute=institute)
    
    faculty = Teacher.objects.filter(employed=institute)

    classes = Class.objects.filter(institute=institute)
    
    context = {'institute':institute, 'events':events, 'students':registered_students, 'faculties':faculty, 'classes':classes}
    
    return render(request, 'app3/college_dashboard.html', context)
    