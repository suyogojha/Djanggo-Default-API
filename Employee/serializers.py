from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields=('id','url','name','department')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Department
        fields=('id','url','name')