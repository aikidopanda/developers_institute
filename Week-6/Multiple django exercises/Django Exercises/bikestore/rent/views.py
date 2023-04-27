from django.shortcuts import render
from .models import *
from .forms import *
from datetime import date
from django.db.models import F
from faker import Faker

fake = Faker()

# Create your views here.


def view_all_rentals(request):
    rentals_list = Rental.objects.all().order_by(
        F('return_date').asc(nulls_first=True))
    context = {
        'rentals_list': rentals_list
    }
    return render(request, 'rentals.html', context)


def view_rental(request, id):
    msg = ''
    rental = Rental.objects.get(id=id)
    if request.method == 'POST':
        form = ReturnVehicle(request.POST)
        if form.is_valid():
            rental.return_date = date.today()
            rental.save()
            msg = 'Vehicle returned'
    else:
        form = ReturnVehicle()
        msg = ''

    context = {
        'rental': rental,
        'id': id,
        'msg': msg,
        'form': form
    }
    return render(request, 'rental.html', context)


def new_rent(request):
    error = False
    vehicle_rented = False
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if not Customer.objects.get(id=data['customer_id']) or not Vehicle.objects.get(id=data['vehicle_id']):
                error = True
            elif Rental.objects.filter(return_date=None):
                vehicle_rented = True
            else:
                new_rent = Rental(rental_date=date.today(), return_date=None, customer=Customer.objects.get(
                    id=data['customer_id']), vehicle=Vehicle.objects.get(id=data['vehicle_id']))
                new_rent.save()
    else:
        form = RentForm()
    context = {
        'error': error,
        'vehicle_rented': vehicle_rented,
        'form': form
    }
    return render(request, 'newrent.html', context)


def view_customer(request, id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer,
        'id': id
    }
    return render(request, 'customer.html', context)


def view_customers(request):
    customers_list = Customer.objects.all().order_by('last_name', 'first_name')
    context = {
        'customers_list': customers_list
    }
    return render(request, 'customers.html', context)

# Ask Yossi how to add phonenumbers via forms input


def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_customer = Customer(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], phonenumber=fake.phone_number(
            ), address=data['address'], city=data['city'], country=data['country'])
            new_customer.save()
    else:
        form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'newcustomer.html', context)


def view_vehicles(request):
    vehicles_list = Vehicle.objects.all().order_by('vehicle_type_id', 'size_id')
    context = {
        'vehicles_list': vehicles_list
    }
    return render(request, 'vehicles.html', context)


def view_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    context = {
        'vehicle': vehicle,
        'id': id
    }
    return render(request, 'vehicle.html', context)

def new_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_vehicle = Vehicle(real_cost=data['real_cost'], size=data['size'], vehicle_type=data['vehicle_type'])
            new_vehicle.save()
    else:
        form = VehicleForm()
    context = {
        'form': form
    }
    return render(request, 'newcustomer.html', context)
