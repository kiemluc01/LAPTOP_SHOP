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
        profile = Userprofile.objects.get(user=request.user)
        user_serializer = ProfileSerializer(profile)
        return Response(user_serializer.data)
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return DetailProductSerializer
    
    @action(detail=True, methods=['GET'])
    def get_image(self, request, pk=None):
        images = Image.objects.filter(product=pk)
        print(ImageSerializer(data=images).data)
        return Response(ImageSerializer(images).data, status=status.HTTP_200_OK)
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class OrderringViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = OrderringSerializer
    
class BillOrderViewset(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillOrderSerializer
    
    
class UserViewset(viewsets.ModelViewSet):
    pass