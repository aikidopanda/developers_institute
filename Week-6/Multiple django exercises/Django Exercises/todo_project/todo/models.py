from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=500)

    def __str__(self):
        return f'Category: {self.name}'
    

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(default=datetime.strptime('2025-01-01', '%Y-%m-%d'), blank=True, null=True)
    deadline_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.details} | {self.date_creation} | {self.deadline_date} | {self.category}'



