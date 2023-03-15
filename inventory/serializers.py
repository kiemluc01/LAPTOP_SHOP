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
        
# class 
