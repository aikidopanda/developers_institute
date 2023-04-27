import os
import django
from faker import Faker
import random
from datetime import timedelta
fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore.settings')
django.setup()

from rent.models import Customer, Vehicle_Size, Vehicle_Type, Rental, Rental_Rate, Vehicle

# populating customers table
# for i in range (150):
#     new_customer = Customer(first_name = fake.first_name(), last_name = fake.last_name(), email = fake.email(), phonenumber = fake.phone_number(), address = fake.address(), city = fake.city(), country = fake.country())
#     new_customer.save()

#populating vehicles
# for i in range(200):
#     size = random.choice(Vehicle_Size.objects.all())
#     type = random.choice(Vehicle_Type.objects.all())
#     cost = random.randint(800,2400)

#     new_vehicle = Vehicle(vehicle_type = type, real_cost = cost, size = size)
#     new_vehicle.save()

# populating rentals
# for i in range(100):
#     fake_date = fake.date_this_decade(before_today = True)
#     randomdelta = random.randint(1,3)
#     fake_future = fake_date + timedelta(days=randomdelta)
#     customer = random.choice(Customer.objects.all())
#     vehicle = random.choice(Vehicle.objects.all())
#     if random.randint(1,20) < 2:
#         fake_future = None
#     rental = Rental(rental_date = fake_date, return_date = fake_future, customer = customer, vehicle = vehicle)
#     rental.save()






