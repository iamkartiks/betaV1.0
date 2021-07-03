from app4.models import CareerOption, Level
from django.shortcuts import render

def levelplay(request):
    levels = Level.objects.all()
    context = {'levels':levels}
    return render(request,'app4/levelbased.html',context)

def career(request):
    careers = CareerOption.objects.all()
    context = {'careers':careers}
    return render(request,'app4/career.html',context)