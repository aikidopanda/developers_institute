"""
URL configuration for bikestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import view_all_rentals, view_rental, new_rent, view_customer, view_customers, new_customer, view_vehicles, view_vehicle, new_vehicle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental', view_all_rentals),
    path('rent/rental/<int:id>',view_rental),
    path('rent/rental/add', new_rent),
    path('rent/customer/<int:id>',view_customer),
    path('rent/customer',view_customers),
    path('rent/customer/add',new_customer),
    path('rent/vehicle',view_vehicles),
    path('rent/vehicle/<int:id>',view_vehicle),
    path('rent/vehicle/add',new_vehicle)
]
