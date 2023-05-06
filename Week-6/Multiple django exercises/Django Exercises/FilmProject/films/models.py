from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    created_in_country = models.ForeignKey(Country, related_name = 'created_in', on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name='available_in', null=True)
    category = models.ManyToManyField(Category, related_name='category')
    director = models.ManyToManyField(Director, related_name='director')

    def __str__(self):
        return f'{self.title} | {self.release_date}'
