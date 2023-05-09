"""
URL configuration for management project.

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
from management_app.views import (DepartmentListAPIView, DepartmentCreateAPIView, DepartmentRetrieveAPIView, EmployeeListAPIView, EmployeeCreateAPIView, EmployeeRetrieveAPIView, ProjectListAPIView, ProjectRetrieveAPIView,
ProjectUpdateAPIView, ProjectDestroyAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', DepartmentListAPIView.as_view(), name = 'departments'),
    path('departments/create', DepartmentCreateAPIView.as_view(), name = 'create_department'),
    path('departments/retrieve/<int:pk>', DepartmentRetrieveAPIView.as_view(), name = 'department-detail'),
    path('employees/', EmployeeListAPIView.as_view(), name = 'employees'),
    path('employees/create', EmployeeCreateAPIView.as_view(), name = 'create_employee'),
    path('employees/retrieve/<int:pk>', EmployeeRetrieveAPIView.as_view(), name = 'employee-detail'),
    path('projects/', ProjectListAPIView.as_view(), name = 'projects'),
    path('projects/retrieve/<int:pk>', ProjectRetrieveAPIView.as_view(), name = 'project-detail'),
    path('projects/update/<int:pk>', ProjectUpdateAPIView.as_view(), name = 'update_project'),
    path('projects/delete/<int:pk>', ProjectDestroyAPIView.as_view(), name = 'delete_project'),
    path('tasks/', TaskListAPIView.as_view(), name = 'tasks'),
    path('tasks/retrieve/<int:pk>', TaskRetrieveAPIView.as_view(), name = 'task-detail'),
    path('tasks/update/<int:pk>', TaskUpdateAPIView.as_view(), name = 'update_task'),
    path('tasks/delete/<int:pk>', TaskDestroyAPIView.as_view(), name = 'delete_task'),
]
