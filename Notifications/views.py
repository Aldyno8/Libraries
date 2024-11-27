from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import * 
from .serialisers import *

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerialiser   
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
class ReadNotifications(APIView):
    def put(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk)
            notification.is_read = True
            notification.save()
            return Response({"message": "lecture de notification"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            
        

    
    