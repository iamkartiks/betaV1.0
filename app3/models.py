from django.db.models.deletion import CASCADE
from app1.views import institutes
from django.db import models
from django.db.models.fields.related import ManyToManyField
from app1.models import *




class Address(models.Model):
    Address1 = models.CharField(max_length=200, null=True)
    Address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=200, null=True)
    postalcode = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True)

    def __repr__(self):
        return self.Address1

    def __str__(self):
        return self.Address1


class Department(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Teacher(models.Model):

    SEX = (('Male', 'Male'),
            ('FEMALE', 'FEMALE'),
            ('OTHERS', 'OTHERS'),
            )

    name = models.CharField(max_length=200,null=True)
    qualification = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    employed = models.ForeignKey(Institutes,null=True, on_delete=CASCADE)
    email = models.CharField(max_length=100, null=True)
    address = models.ManyToManyField(Address)
    specialised = models.ManyToManyField(Department)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class RegisteredStudent(models.Model):

    SEX = (('Male', 'Male'),
            ('FEMALE', 'FEMALE'),
            ('OTHERS', 'OTHERS'),
            )

    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    dob = models.DateField(max_length=8)
    sex = models.CharField(max_length=100, null=True, choices=SEX)
    ethnicity = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.ManyToManyField(Address)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Registered(models.Model):
    institute = models.ForeignKey(Institutes, null=True, on_delete=models.SET_NULL)
    students = models.OneToOneField(RegisteredStudent, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return self.institute.name
    
    def __str__(self):
        return self.institute.name


class Class(models.Model):
    name = models.CharField(max_length=200, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    students = models.ManyToManyField(RegisteredStudent)
    institute = models.ForeignKey(Institutes, null=True, on_delete=models.SET_NULL)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Progress(models.Model):
    refrence_class = models.ManyToManyField(Class)
    student = models.ManyToManyField(RegisteredStudent)


class Payment(models.Model):
    TYPE = (('fee', 'fee'),
           ('salary', 'salary'),
           ('others', 'others')
           )

    amount = models.IntegerField(null=True)
    type = models.CharField(max_length=100, null=True, choices=TYPE)

    def __repr__(self):
        return self.amount

    def __str__(self):
        return self.amount


class Institute(models.Model):
    institute = models.OneToOneField(Institutes, on_delete=models.CASCADE)

    def __repr__(self):
        return self.institute.name

    def __str__(self):
        return self.institute.name
