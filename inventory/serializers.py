from rest_framework import serializers
from inventory.models import Inventory, InventoryIn, InventoryInItem, InventoryItem, InventoryOut, InventoryOutItem

class InventorySerrializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fileds = '__all__'
        
class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields ='__all__'
        
class InventoryInSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryIn
        fields = '__all__'
        
class InventoryInItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryInItem
        fields = '__all__'
        
class InventoryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryOut
        fields = '__all__'
        
class InventoryOutItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryOutItem
        fields = '__all__'
