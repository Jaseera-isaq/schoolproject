from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
