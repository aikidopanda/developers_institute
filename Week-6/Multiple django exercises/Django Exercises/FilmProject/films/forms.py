from django import forms
from .models import *

class AddFilmForm(forms.ModelForm):
    
    class Meta:
        model = Film
        fields = '__all__'


class AddDirectorForm(forms.Form):
    first_name = forms.CharField(label="Director's first name")
    last_name = forms.CharField(label='And his/her last name')