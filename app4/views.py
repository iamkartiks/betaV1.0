from app4.models import CareerOption, Level, Problems
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

def levelpage(request,pk):
    problems = Problems.objects.filter(id=pk)
    level = Level.objects.get(id=pk)
    context = {'level':level, 'problems':problems}
    return render(request,'app4/levelpage.html', context)