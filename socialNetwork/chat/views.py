from django.shortcuts import render
from rest_framework import generics
from .models import  Message#ChatUser,
from .serializers import MessageSerializer#ChatUserSerializer,
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# class ChatUserListCreateView(generics.ListCreateAPIView):
    # queryset = ChatUser.objects.all()
    # serializer_class = ChatUserSerializer

@swagger_auto_schema(method='post', request_body=MessageSerializer)
@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.create(serializer.validated_data)
        # Additional logic for handling the created message
        return Response({"message": "Message created successfully"})
    return Response(serializer.errors, status=401)
