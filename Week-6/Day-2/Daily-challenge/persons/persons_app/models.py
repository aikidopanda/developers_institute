from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.TextField()

# Create your models here.
