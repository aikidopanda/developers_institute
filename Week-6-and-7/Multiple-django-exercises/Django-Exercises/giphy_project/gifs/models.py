from django.db import models

# Create your models here.


class Gif_Model(models.Model):

    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}, uploaded by {self.uploader_name}, created at {self.created_at}'


class Category(models.Model):

    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif_Model) #try (Gif_Model, related_name = 'categories') and then use it

    def __str__(self):
        return f'{self.name}'
