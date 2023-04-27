from django.contrib import admin

from rent.models import Rental_Rate, Customer, Vehicle, Vehicle_Size, Vehicle_Type, Rental

# Register your models here.

admin.site.register(Rental)
admin.site.register(Rental_Rate)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Vehicle_Size)
admin.site.register(Vehicle_Type)


