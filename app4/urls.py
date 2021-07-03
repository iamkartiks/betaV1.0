from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('level/',views.levelplay, name='levelbased'),
    path('ecareer/',views.career, name='career'),

]
