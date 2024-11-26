from rest_framework import serializers
from .models import *

class MessageSerialiser(serializers.ModelSerializer):
   class Meta:
        model = ForumMessage
        fields = ['message', 'author', 'created_at']
        
class SubjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ForumSubject
        fields = ['id', 'subject']