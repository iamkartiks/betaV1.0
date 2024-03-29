from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('dashboard/<str:pk>', views.dashboard, name="dashboard"),
    # path('collegeboard',views.collegeportal, name="portal"),
    path('institutes/',views.institutes, name="institutes"),
    path('course/',views.course, name="course"),
    path('completeprofile/',views.complete, name="ccomplete"),
    path('institute/<str:pk>', views.privinstitute, name="privins"),
    path('getstarted/', views.getstarted, name="getstart"),
    path('jobportal/', views.joblist, name="jobportal"),
    path('jobapply/<str:pk>',views.jobapplication, name="jobapply"),
    path('faq/',views.faq,name="faq"),
    path('events/',views.event, name="event")
]
