from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# class LoginForm(forms.Form):

#     Username = forms.CharField()
#     Password = forms.PasswordInput()
