from rest_framework import serializers
from .models import *

class MessageSerialiser(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = ForumMessage
        fields = ['message', 'author_name', 'created_at']
        
class SubjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ForumSubject
        fields = ['id', 'subject']