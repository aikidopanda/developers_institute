from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ManyToManyField('Project')

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField()
    project = models.ManyToManyField('Project')

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f'{self.name}'