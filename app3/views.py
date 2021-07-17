from django.shortcuts import render
from .models import *
from app1.models import *
from app4.models import *

def managementsys(request):
    return render(request, 'app3/managementsys.html')

def dashboard(request, pk):
    institute = Institutes.objects.get(id=pk)
    events = Event.objects.filter(institute=institute)
    context = {'institute':institute, 'events':events}
    return render(request, 'app3/college_dashboard.html', context)