from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, 
HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT)
from rest_framework.permissions import AllowAny
from rest_framework import generics

# Create your views here.

class DepartmentListAPIView(generics.ListAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)

class DepartmentCreateAPIView(generics.CreateAPIView):

    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)

class EmployeeListAPIView(generics.ListAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)

class EmployeeCreateAPIView(generics.CreateAPIView):

    model = Employee
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)

class ProjectRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(generics.UpdateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def put(self, request, pk, *args, **kwargs):

        project = Project.objects.get(pk = pk)
        serializer = ProjectSerializer(project, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ProjectDestroyAPIView(generics.DestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(generics.UpdateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def put(self, request, pk, *args, **kwargs):

        task = Task.objects.get(pk = pk)
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class TaskDestroyAPIView(generics.DestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer



    


