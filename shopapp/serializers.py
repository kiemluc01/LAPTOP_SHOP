from rest_framework import serializers
from .models import User,Userprofile, ProductCategory, BaseProduct, Comment, Image, Cart, CartItem, Bill, BillItem, UserPolicy
from django.contrib.auth import authenticate

    
# class ProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Userprofile
#         fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid username or password')
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
        model = BaseProduct
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
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
        model = Cart
        fields = '__all__'
        
class BillOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'