from django import forms
from .models import *

class AddFilmForm(forms.Form):
    title = forms.CharField(label='Title')
    release_date = forms.DateField(label='Release date')
    created_in_country  = forms.CharField(label='Country of creation')
    available_in_countries = forms.ModelChoiceField(queryset = Country.objects.all())
    director = forms.CharField(label='Director')


class AddDirectorForm(forms.Form):
    first_name = forms.CharField(label="Director's first name")
    last_name = forms.CharField(label='And his/her last name')