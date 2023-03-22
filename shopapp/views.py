from django.shortcuts import render
from rest_framework import viewsets, status, permissions, generics, views
import django_filters
from django_filters import FilterSet
from .models import *
from .serializers import *
from rest_framework.decorators import action
from knox.views import LoginView
from django.contrib.auth import login
from rest_framework.response import Response
    
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
    
class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
    
class UserViewset(viewsets.ModelViewSet):
    pass