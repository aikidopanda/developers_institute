from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', 'title', 'description')