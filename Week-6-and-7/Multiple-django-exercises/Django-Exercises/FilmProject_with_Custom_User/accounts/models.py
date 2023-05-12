from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField(blank=True, null=True)
#     films_reviewed = models.IntegerField(default=0, blank=True)

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'


# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender = User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# Create your models here.

class UserManager(BaseUserManager): # manager that define user and superuser methods
    def create_user(self, email, password, **extra_fields): # create and save a new user with the given email and password
        if not email:
            raise ValueError('PLease add your email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields): # creates and save a superuser with the given email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True) # standard fields of AbstractBaseUser
    last_name = models.CharField(max_length=50, blank=True) # standard fields of AbstractBaseUser
    date_joined = models.DateTimeField(auto_now_add=True) # standard fields of AbstractBaseUser
    is_active = models.BooleanField(default=True) # standard fields of AbstractBaseUser
    is_staff = models.BooleanField(default=False) # standard fields of AbstractBaseUser

    USERNAME_FIELD = 'email' # unique id, needs for authenticate
    REQUIRED_FIELDS = ['first_name', 'last_name'] # field when superuser create

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self): # optional attr
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self): # optional attr
        return self.first_name    
