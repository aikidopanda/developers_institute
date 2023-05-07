from django.db import models

# Create your models here.

# "id" :1,
# "name": "Dog",
# "legs": 4,
# "weight": 5.67,
# "height":4.2,
# "speed": 34,
# "family": 2

# "id": 1;,
# "name": "Caninae"

class Family(models.Model):
    name = models.CharField(max_length=50) # varchar

class Animal(models.Model):
    name = models.CharField(max_length=50)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)


#to create, for example: felidae = Family(name = 'Felidae')


