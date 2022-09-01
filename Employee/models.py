from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.name