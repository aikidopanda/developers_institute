from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class NameForm(forms.Form):
    search_name = forms.CharField(label="Search people by name", max_length=100)

class PhoneForm(forms.Form):
    search_phone = forms.CharField(label='Search people by phone number', max_length=20)