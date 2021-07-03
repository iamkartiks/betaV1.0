from django.db import models

class CareerOption(models.Model):
    name = models.CharField(max_length=100,null=True)
    total_levels = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100,null=True)
    Topic = models.CharField(max_length=100,null=True)
    career= models.ForeignKey(CareerOption, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name
