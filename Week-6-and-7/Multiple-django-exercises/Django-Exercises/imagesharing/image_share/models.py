from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Image(models.Model):
    file = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, {self.images}'


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Image)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.user.profile.images += 1
        instance.user.profile.save()
