from django.db import models
from app1.models import *

class CareerOption(models.Model):
    name = models.CharField(max_length=100,null=True)
    total_levels = models.CharField(max_length=100,null=True)
    student = models.ManyToManyField(Student)
    

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100,null=True)
    Topic = models.CharField(max_length=100,null=True)
    career= models.ForeignKey(CareerOption, null=True, on_delete= models.SET_NULL)
    
    
    def __str__(self):
        return self.name


class StudentLevel(models.Model):

    career = models.ForeignKey(CareerOption,null=True, on_delete= models.SET_NULL)
    student = models.ForeignKey(Student,null=True, on_delete= models.SET_NULL)
    level = models.ForeignKey(Level,null=True, on_delete= models.SET_NULL)
    
    
    def __str__(self):
        return self.level.name

class CareerStatus(models.Model):

    STATUS = (('NC', 'Not Completed'),
                ('C', 'Completed')
                )
    careeropt = models.ForeignKey(CareerOption,null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.status