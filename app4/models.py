from django.db import models
from django.db.models import Deferrable, UniqueConstraint
import uuid

from django.db.models.aggregates import Max
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
    
    def __repr__(self):
        return self.name


    def __str__(self):
        return self.name


class StudentLevel(models.Model):

    career = models.ForeignKey(CareerOption,null=True, on_delete= models.SET_NULL)
    student = models.ForeignKey(Student,null=True, on_delete= models.SET_NULL)
    level = models.ForeignKey(Level,null=True, on_delete= models.SET_NULL)

    # UniqueConstraint(fields = ['level', 'key2'], name = 'constraint_name')
    
    def __repr__(self):
        return self.level.name


    def __str__(self):
        return self.level.name

class CareerStatus(models.Model):

    STATUS = (('NC', 'Not Completed'),
                ('C', 'Completed')
                )
    careeropt = models.ForeignKey(CareerOption,null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True, choices=STATUS)


    def __repr__(self):
        return self.status

    def __str__(self):
        return self.status


class Task(models.Model):

    STATUS = (('Incomplete', 'Incomplete'),
              ('Complete', 'Complete')
              )
    name = models.CharField(max_length=200,null=True)
    task_type = models.CharField(max_length=100, null=True)
    student = models.ForeignKey(Student,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    STATUS  = (('Accepted', 'Accepted'),
                ('In Progress', 'In Progress'),
                ('Rejected', 'Rejected')
                )
    jobno = models.CharField(max_length=100, blank=True, unique=True)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    student = models.ForeignKey(Student,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name