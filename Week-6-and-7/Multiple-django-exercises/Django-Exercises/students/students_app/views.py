from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, 
HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT)
from rest_framework.permissions import AllowAny
from rest_framework import generics

# Create your views here.

class StudentsList(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    # def get(self, request, *args, **kwargs):

    #     students = Student.objects.all()
    #     serializer = StudentSerializer(students, many = True)

    #     return Response(serializer.data)
    
    def get_queryset(self):
        date_joined = self.request.query_params.get('date_joined')
        # queryset = Student.objects.all()
        if date_joined:
            queryset = Student.objects.filter(date_joined=date_joined)
        else:
            queryset = Student.objects.all()

        return queryset
    
    def post(self, request, *args, **kwargs):

        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):

    def get(self, request, *args, **kwargs):

        permission_classes = (AllowAny,)

        pk = kwargs.get('pk')

        if pk:
            try:             
                student = Student.objects.get(id = pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_404_NOT_FOUND)
            
    def put(self, request, pk, *args, **kwargs):

        student = Student.objects.get(pk = pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)






