from rest_framework import serializers
from inventory.models import Inventory, InventoryIn, InventoryInItem, InventoryItem, Province, District, Ward


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields =  '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

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
        