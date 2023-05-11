from django import forms
from .models import *

class AddFilmForm(forms.ModelForm):
    
    class Meta:
        model = Film
        fields = '__all__'


class AddDirectorForm(forms.Form):
    first_name = forms.CharField(label="Director's first name")
    last_name = forms.CharField(label='And his/her last name')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']