from rest_framework import serializers
from .models import User,Userprofile, Department, CreditCard, ProductCategory, Product, DetailProduct, Comment, Image, Orderring, BillOrder

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__' #['name', 'code']
         
    def __str__(self):
        return 'Department<{}>: {}'.format(self.pk, self.name)
    
class CreditcardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreditCard
        fields = '__all__'
        
    def __str__(self):
        return 'Creditcard<{}>: {}'.format(self.pk, self.code)
    
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Userprofile
        fields = '__all__'
        
    def __str__(self):
        return 'Profile<{}>: {}'.format(self.pk, self.user)


class UserSerializer(serializers.ModelSerializer):
    
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        exclude =  ['password', 'user_permissions', 'is_superuser', 'is_staff']
        
    def __str__(self):
        return 'User<{}>: {}'.format(self.pk, self.username)
    
class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fileds =  ['id', 'username', 'email', 'Profile']
        
    def __str__(self):
        return 'User<{}>: {}'.format(self.pk, self.username)
