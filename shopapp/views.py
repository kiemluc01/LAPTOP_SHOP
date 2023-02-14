from django.shortcuts import render
from rest_framework import viewsets, status
import django_filters
from django_filters import FilterSet
from .models import *
from .serializers import *
from rest_framework.decorators import action


# Create your views here.

class DepartmentFilter(FilterSet):
    name = django_filters.CharFilter("Name", max_length=150, lookup_expr='icontains')
    class Meta:
        model = Department
        fields = ['name']
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = departmentSerializer
    filterset_class = DepartmentFilter
    