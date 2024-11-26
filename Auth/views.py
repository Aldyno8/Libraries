from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Auth import serialisers

class UserRegister(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = serialisers.UserSerialiser
        permission_classes = [AllowAny]
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serialisers.UserSerialiser
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serialisers.UserSerialiser

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serialisers.UserSerialiser