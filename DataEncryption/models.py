from django.db import models

# Create your models here.
class Employee(models.Model):
    age = models.IntegerField()
    salary = models.IntegerField()