from rest_framework import serializers
from chatbox.models import HistoryChat, ProductHistory, StaffHistorychat
from shopapp.serializers import ProductSerializer, ProfileSerializer

class HistoryChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoryChat
        fields = '__all__'
        
class ProductHistorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductHistory
        fields = '__all__'
        
class StaffHistorySerializer(serializers.ModelSerializer):
    staff = ProfileSerializer(read_only=True)
    
    class Meta:
        model = StaffHistorychat
        fields = '__all__'
class DetailHistorychatSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    staff = StaffHistorySerializer(read_only=True)
    class Meta:
        model = HistoryChat
        fields = '__all__'