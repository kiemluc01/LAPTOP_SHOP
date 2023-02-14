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
    
class CreditCardViewset(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditcardSerializer
    
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Userprofile.objects.all()
    serializer_class = ProfileSerializer
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return DetailProductSerializer
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class OrderringViewset(viewsets.ModelViewSet):
    queryset = Orderring.objects.all()
    serializer_class = OrderringSerializer
    
class BillOrderViewset(viewsets.ModelViewSet):
    queryset = BillOrder.objects.all()
    serializer_class = BillOrderSerializer
    