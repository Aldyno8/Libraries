from rest_framework import serializers
from .models import *

class NotificationSerialiser(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Notification
        fields = ['user_name', 'created_at', 'message', 'url', 'is_read']
        
    