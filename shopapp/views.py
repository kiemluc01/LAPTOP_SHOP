from django.shortcuts import render
from rest_framework import viewsets, status, views, generics
import django_filters
from django_filters import FilterSet
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
    
class UserPolicyViewset(viewsets.ModelViewSet):
    queryset = UserPolicy.objects.all()
    serializer_class = UserPolicySerializer
class Profile(views.APIView):
    def get(self, request):
        profile = User.objects.filter(pk=request.user.id).first()
        print(profile.password)
        user_serializer = ProfileSerializer(profile)
        return Response(user_serializer.data)
    
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'], is_staff=True)
        user.save()
        return Response(ProfileSerializer(user).data)
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    
class FilterProduct(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")
class ProductViewset(viewsets.ModelViewSet):
    queryset = BaseProduct.objects.all()
    serializer_class = DetailProductSerializer
    filterset_class = FilterProduct
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            print('retrieve')
            return DetailProductSerializer
        return ProductSerializer
    
    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        images = Image.objects.filter(product=pk)
        return Response(ImageSerializer(images).data, status=status.HTTP_200_OK)
    
    
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    
    
class OrderringViewset(views.APIView):
    
    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        return Response(OrderringSerializer(cart).data)
    
class BillOrderViewset(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillOrderSerializer
    
    
class UserViewset(viewsets.ModelViewSet):
    pass