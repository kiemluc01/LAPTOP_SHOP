from django.shortcuts import render
from rest_framework import viewsets, status, views, generics
import django_filters
from django_filters import FilterSet
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
    
class UserPolicyViewset(viewsets.ModelViewSet):
    queryset = UserPolicy.objects.all()
    serializer_class = UserPolicySerializer
class Profile(views.APIView):
    def get(self, request):
        # profile = User.objects.filter(pk=request.user.id).first()
        profile = request.user
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
    permission_classes = (AllowAny,)
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
    permission_classes = (AllowAny,)
    
class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class OrderringViewset(views.APIView):
    ordering = ["created_at"]
    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        return Response(OrderringSerializer(cart).data)
    
    def post(self, request):
        cart_serializer = CartListSerializer(data=request.user)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_serializer.data, status=status.HTTP_400_BAD_REQUEST)
class BillOrderViewset(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillOrderSerializer
    
class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer   
    ordering = ["-id"]
    
    
    
class UserViewset(viewsets.ModelViewSet):
    pass