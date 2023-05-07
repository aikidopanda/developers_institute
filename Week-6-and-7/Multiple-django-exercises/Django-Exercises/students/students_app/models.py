from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
