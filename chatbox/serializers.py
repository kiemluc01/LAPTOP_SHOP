from rest_framework import serializers
from chatbox.models import HistoryChat

class HistoryChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryChat
        fields = '__all__'
        
        