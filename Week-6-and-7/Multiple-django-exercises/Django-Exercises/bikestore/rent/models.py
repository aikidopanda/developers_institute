from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from faker import Faker

fake = Faker()

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = PhoneNumberField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vehicle_Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Vehicle_Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.IntegerField()
    size = models.ForeignKey(Vehicle_Size, on_delete=models.DO_NOTHING)

    def _str_(self):
        return f'{self.vehicle_type} of {self.size}'


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'The {self.vehicle.size} {self.vehicle.vehicle_type}, rented on {self.rental_date} by {self.customer}, returned on {self.return_date}'


class Rental_Rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.DO_NOTHING)
    vehicle_size = models.ForeignKey(Vehicle_Size, on_delete=models.DO_NOTHING)
