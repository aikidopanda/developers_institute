from django import forms
from .models import Category, Gif_Model

class GifForm(forms.Form):
    uploader_name = forms.CharField(label = 'Enter your name', max_length=50)
    title = forms.CharField(label = 'Enter the file name', max_length=100)
    url = forms.URLField(max_length=500)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    exclude = ('likes')


class CategoryForm(forms.Form):
    name = forms.CharField(label='Enter the name of new category', max_length=50)


class LikeForm(forms.Form):
    gif = forms.ModelChoiceField(queryset=Gif_Model.objects.all(), widget=forms.HiddenInput())
    like = forms.BooleanField(required = False, widget=forms.HiddenInput())
    # use list(zip) function to connect buttons with gifs