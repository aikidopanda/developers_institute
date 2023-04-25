from django import forms
from .models import Category,ToDo
from datetime import date, datetime

class ToDoForm(forms.Form):
    title = forms.CharField(max_length=50)
    details = forms.CharField(widget=forms.Textarea())
    has_been_done = forms.BooleanField(required=False)
    date_completion = forms.DateTimeField(required=False)
    deadline_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())

