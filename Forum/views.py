from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serialisers import *

class CreateForum(APIView):
    def post(self, request):
        author = request.user
        subject = request.data.get('subject')
        try:
            ForumSubject.objects.create(
                subject=subject,
                creator=author
            )
            return Response({"message": "Forum created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            
class CreateMessage(APIView):
    def post(self, request):
        id_forum = request.data.get('id')
        message = request.data.get('message')
        author = request.user
        try:
            forum = ForumSubject.objects.get(id=id_forum)
            ForumMessage.objects.create(
                subject=forum,
                message=message,
                author=author
            )
            return Response({"message": "message send successfully"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

class ForumListView(APIView):
    def get(self, request):
        try:
            forum = ForumSubject.objects.all()
            serializer = SubjectSerialiser(forum, many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)    
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

class ForumDetails(APIView):
    def get(self, request, pk):
        
        try:
            forum_id = pk
            print(pk)

            if not forum_id:
                return Response({"message": "Forum ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                forum = ForumSubject.objects.get(id=forum_id)
            except ForumSubject.DoesNotExist:
                return Response({"message": "Forum not found."}, status=status.HTTP_404_NOT_FOUND)

            
            forum_serializer = SubjectSerialiser(forum)
            
            messages = ForumMessage.objects.filter(subject=forum)
            message_serializer = MessageSerialiser(messages, many=True)

            response_data = {
                "forum": forum_serializer.data,
                "messages": message_serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            
            