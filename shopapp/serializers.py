from rest_framework import serializers
from .models import User,Userprofile, ProductCategory, Product, Comment, Image, Orderring, BillOrder, UserPolicy
from django.contrib.auth import authenticate
    
# class ProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Userprofile
#         fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'
class LoginSerializer(serializers.ModelSerializer):
    username_log = serializers.CharField(max_length=150)
    password_log = serializers.CharField(max_length=150,style={'input_type': 'password'}, trim_whitespace=False)

    
    class Meta:
        model = User
        fields = ['username_log', 'password_log']
        
    def validate(self, attrs):
        username_log = attrs.get('username_log')
        password_log = attrs.get('password_log')
        if username_log and password_log:
            if User.objects.filter(username=username_log,is_staff=True,is_active=True).exists():
                user = authenticate(request=self.context.get('request'),username=username_log, password=password_log)
            else:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)
            if not user:
                msg = {
                    'detail': 'Password error.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPolicy
        fields = '__all__'
    
class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fileds =  ['id', 'username', 'email', 'Profile']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'rootImage', 'price']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
class OrderringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderring
        fields = '__all__'
        
class BillOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOrder
        fields = '__all__'