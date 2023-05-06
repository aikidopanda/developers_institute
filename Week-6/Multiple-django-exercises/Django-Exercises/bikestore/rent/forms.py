from django import forms
from .models import Vehicle_Size, Vehicle_Type

class RentForm(forms.Form):
    customer_id = forms.IntegerField(label = 'Enter a customer id')
    vehicle_id = forms.IntegerField(label = 'Enter a vehicle id')


class CustomerForm(forms.Form):
    first_name = forms.CharField(label = 'Enter your first name')
    last_name = forms.CharField(label = 'Enter your last name')
    email = forms.EmailField(label = 'Enter your email')
    phonenumber = forms.IntegerField (label = 'Enter your phone number')
    address = forms.CharField(label = 'Enter your address')
    city = forms.CharField(label = 'Enter your city')
    country = forms.CharField(label = 'And your country')


class VehicleForm(forms.Form):
    real_cost = forms.IntegerField()
    size = forms.ModelChoiceField(queryset = Vehicle_Size.objects.all())
    vehicle_type = forms.ModelChoiceField(queryset = Vehicle_Type.objects.all())


class ReturnVehicle(forms.Form):
    return_vehicle = forms.BooleanField(required = False, widget=forms.HiddenInput())

