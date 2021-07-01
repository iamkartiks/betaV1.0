from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('blog/',views.blog, name='blog'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path('collegeboard',views.collegeportal, name="portal"),
]
