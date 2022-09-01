from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Employee,Department
from .serializers import EmployeeSerializer,DepartmentSerializer

# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly,)