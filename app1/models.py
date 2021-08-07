from types import MappingProxyType
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import  SET_NULL



class Student(models.Model):
    STATUS = (('NA', 'NA'),
              ('highschool', 'highschool'),
              ('undergraduate', 'undergraduate'),
              ('postgraduate', 'postgraduate'),
              ('dropout', 'dropout'),
              )
    user = models.OneToOneField(User, null=True,blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=100, null=True,)
    username = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True,)
    email = models.CharField(max_length=100, null=True,)
    career_status = models.CharField(max_length=200, null=True, choices=STATUS)
    interest = models.CharField(max_length=200,null=True)
    profile = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name

    @property
    def profileURL(self):
        try:
            url = self.profile.url
        except:
            url = ''
        return url


class Label(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Institutes(models.Model):
    CATEGORY = (('playschool', 'playschool'),
                ('highschool', 'highschool'),
                ('college','college'),
                )
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200,null=True)
    fees = models.FloatField(null=True)
    photo = models.ImageField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    label = models.ManyToManyField(Label)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    qsrank = models.IntegerField(null=True)
    sexratio = models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.name

    @property
    def profileURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name



class Application(models.Model):
    STATUS = (('Under Review', 'Under Review'),
              ('Accepted','Accepted'),
              ('Rejected', 'Rejected'),
              )
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    institute = models.ForeignKey(Institutes, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.institute.name

class Course(models.Model):
    CAT = (('Engineering', 'Engineering'),
            ('Entrepreneurship', 'Entrepreneurship'),
            ('Writer', 'Writer'),
            ('Mock Job Course', 'Mock Job Course'))
    name = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=100,null=True,choices=CAT)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name
    

class Enrolled(models.Model):
    institute = models.ForeignKey(Institutes,null=True, on_delete=SET_NULL)
    student = models.OneToOneField(Student, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.institute.name


class PostImage(models.Model):
    image = models.ImageField(null=True)
    institute = models.ForeignKey(Institutes,null=True, on_delete=SET_NULL)

    def __repr__(self):
        return self.institute.name

    def __str__(self):
        return self.institute.name
    

class Program(models.Model):
    name = models.CharField(max_length=200, null=True)
    institute = models.ManyToManyField(Institutes)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200,null=True)
    institute = models.ForeignKey(Institutes,null=True,on_delete=SET_NULL)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    CATEGORY = (('highschool', 'highschool'),
                ('undergraduate', 'undergraduate'),
                ('postgraduate', 'postgraduate'),
                )

    TYPE = (('academics', 'academics'),
            ('competition', 'competition'),
            ('sports', 'sports'),
            ('CCA', 'CCA'),
            )
    name = models.CharField(max_length=200,null=True)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=SET_NULL)
    institute =  models.ManyToManyField(Institutes)
    applicable = models.CharField(max_length=100, null=True, choices=CATEGORY)
    scholarship_type = models.CharField(max_length=100, null=True, choices=TYPE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class PremiumService(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Job(models.Model):

    CAT = (('Internship', 'Intersnhips'),
            ('Full Time Job', 'Full Time Job')
            )
    jname = models.CharField(max_length=100, null=True)
    cname = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True, choices=CAT)
    photo = models.ImageField(null=True)
    requirements = models.CharField(max_length=300, null=True)

    def __repr__(self):
        return self.cname
    
    def __str__(self):
        return self.cname

    @property
    def imageURL(self):
        try: 
            url=self.photo.url
        except:
            url=""
        return url