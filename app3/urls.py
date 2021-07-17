from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('instituteportal/',views.managementsys, name='managementsystem'),
    path('portal/<str:pk>',views.dashboard, name='portaldashboard'),

]
