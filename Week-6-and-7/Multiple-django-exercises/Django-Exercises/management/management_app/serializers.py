from rest_framework import serializers
from .models import Department, Employee, Task, Project

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.HyperlinkedIdentityField(view_name = 'department-detail')

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.HyperlinkedIdentityField(view_name='employee-detail')

    class Meta:
        model = Employee
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.HyperlinkedIdentityField(view_name='task-detail')

    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = Project
        fields = '__all__'

    



