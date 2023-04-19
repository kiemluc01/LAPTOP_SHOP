from rest_framework import serializers
from .models import User,Userprofile, ProductCategory, BaseProduct, Comment, Image, Cart, CartItem, Bill, BillItem, UserPolicy
from inventory.serializers import InventoryItemSerializer

    
class ProfileListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Userprofile
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    profile_user = ProfileListSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_user')
class UserPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPolicy
        fields = '__all__'
    
class UserListSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields =  ['id', 'username', 'email']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class DetailProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    
    class Meta:
        model = BaseProduct
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    inventory_item_product = InventoryItemSerializer(many=True, read_only=True)
    class Meta:
        model = BaseProduct
        fields = ['id', 'name', 'rootImage', 'price', 'inventory_item_product']
        
class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = ['id', 'name', 'rootImage', 'price']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
      
class CartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'  
    
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductCartSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = '__all__'
class OrderringSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'
    def get_items(self, instance):
        items = instance.items.all().order_by('created_at')
        return CartItemSerializer(items, many=True).data
class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class BillOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        

