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
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import  render_to_string
from datetime import datetime

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
    
class RegisterViewset(viewsets.ModelViewSet):
    queryset = User.objects.filter(pk=0)
    serializer_class = UserListSerializer
    permission_classes = [AllowAny,]
    
    @action(detail=False, methods=['post'])
    def send_code(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            return Response({"message":"email {} đã tại trên hệ thống".format(request.data['email'])}, status=status.HTTP_226_IM_USED)
        code = random.randint(100000, 999999)
        mail_from = settings.EMAIL_HOST_USER
        mail_to = request.data['email']
        subject = "XÁC THỰC EMAIL"
        data = {'mail_from': mail_from, 'mail_to':mail_to,'subject':subject}
        time = datetime.now()
        time = time.strftime('%H:%M:%S - %d:%m:%y')
        content = { 
                   "code": code,
                   "time":time,
                   "email": mail_to,
        }
        subject, from_email, to = data['subject'], data['mail_from'], data['mail_to']
        html_content = render_to_string('sendmail.html',context=content)
        msg = EmailMultiAlternatives(subject, None, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response({"code":code},status=status.HTTP_200_OK)

        


        return Response({"code":code}, status=status.HTTP_208_ALREADY_REPORTED)
    @action(detail=False, methods=['post'])
    def user_exists(self, request):
        if User.objects.filter(username=request.data['username']).exists():
            return Response({'result': True}, status=status.HTTP_409_CONFLICT)
        return Response({'result': False}, status=status.HTTP_200_OK)
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
    
    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user.id)
        if CartItem.objects.filter(product=request.data['product'], cart=cart.id).exists():
            item = CartItem.objects.filter(product=request.data['product'], cart=cart.id).first()
            item.quantity+=1
            item.save()
            return Response(CartItemListSerializer(item).data, status=status.HTTP_201_CREATED)
        request.data['cart'] = cart.id
        cart_item_serializer = CartItemListSerializer(data=request.data)
        if cart_item_serializer.is_valid():
            cart_item_serializer.save()
            return Response(cart_item_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_item_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class UserViewset(viewsets.ModelViewSet):
    pass