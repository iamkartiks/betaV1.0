from app4.models import CareerOption, Level
from django.shortcuts import render

def levelplay(request,pk):
    career = CareerOption.objects.get(id=pk)
    levels = career.level_set.all()
    context = {'levels':levels,'career':career}
    return render(request,'app4/levelbased.html',context)

def career(request):
    career = CareerOption.objects.all()
    context = {'career':career}
    return render(request,'app4/career.html',context)