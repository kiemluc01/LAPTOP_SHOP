from django.shortcuts import render
from rest_framework import viewsets
from inventory.models import Province, District, Ward
from inventory.serializers import ProvinceSerializer, DistrictSerializer, WardSerializer

# Create your views here.
class ProvinceViewset(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    
class DistrictViewset(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    
class WardViewset(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer