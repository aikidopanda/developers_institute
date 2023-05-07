from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.TextField()

    def __str__(self):
        return f'{self.name} | {self.phone_number} | {self.address} | {self.email}'

# Create your models here.
