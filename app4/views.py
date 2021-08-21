from app4.models import CareerOption, Level
from django.shortcuts import render
from app1.models import Course

def levelplay(request,pk):
    career = CareerOption.objects.get(id=pk)
    levels = career.level_set.all()
    context = {'levels':levels,'career':career}
    return render(request,'app4/levelbased.html',context)

def career(request):
    courses = Course.objects.all()
    careers = CareerOption.objects.all()
    context = {'careers':careers,'courses':courses}
    return render(request,'app4/career.html',context)