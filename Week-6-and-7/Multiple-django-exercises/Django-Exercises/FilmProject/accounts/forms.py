from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# class CustomSignUpForm(UserCreationForm):

#     class Meta (UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + ("film_reviewed",)



class UserProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        exclude = ['user']



# class LoginForm(forms.Form):

#     Username = forms.CharField()
#     Password = forms.PasswordInput()
