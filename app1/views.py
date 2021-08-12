from app4.models import *
from app1.models import Institutes
from typing import ContextManager
from django.shortcuts import render
from .models import *
from django.db.models import Count


def index(request):
    context={}
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
    student = Student.objects.get(id=pk)
    career = [c.name for c in student.careeroption_set.all()]
    applications = student.application_set.all()
    current_level =  StudentLevel.objects.filter(student=student)

    tasks = student.task_set.all()

    career_status = [ c.status for c in CareerStatus.objects.filter(student=student)]
    levelList = [level.level for level in current_level]
    careers = zip(career, levelList, career_status)

    job_applications = student.jobapplication_set.all()

    academics = student.academics_set.all()
    
    enroll = Enrolled.objects.get(student=student)

    context = {'student':student, 'applications':applications,'careers':careers, 'careerstatus':career_status, 'tasks':tasks, 'jobapplications':job_applications, 'academics':academics, 'enroll':enroll}
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


def getstarted(request):
    return render(request, 'app1/getstart.html')


def privinstitute(request,pk):
    institute = Institutes.objects.get(id=pk)
    photos = PostImage.objects.filter(institute=institute)

    labels = Label.objects.filter(institutes=institute)

    total_students = Enrolled.objects.filter(institute=institute).count()

    total_programs = Program.objects.filter(institute=institute).count()
    programs = Program.objects.filter(institute=institute)
    
    events = Event.objects.filter(institute=institute)

    total_scholarships = Scholarship.objects.filter(institute = institute).count()

    scholarship = Scholarship.objects.filter(institute = institute)

    premiums = PremiumService.objects.all()

    context = {'institute':institute, 'photos':photos, 'enrolled_students':total_students, 'labels':labels, 'total_programs':total_programs, 'programs':programs, 'events':events, 'scholarships':scholarship, 'totalscholarships':total_scholarships, 'premiums':premiums}
    
    return render(request,'app1/privateins.html',context)


def joblist(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request, 'app1/jobportal.html', context)