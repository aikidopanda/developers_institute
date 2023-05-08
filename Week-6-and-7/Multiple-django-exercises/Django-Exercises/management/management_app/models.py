from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    employee = models.ManyToManyField(Employee)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return f'{self.name}'