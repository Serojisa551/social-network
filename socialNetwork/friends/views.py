from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .serializers import * 
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages


# Working only with Swagger
@swagger_auto_schema(method='post', request_body=CreatefriendSerializer)
@api_view(['POST'])
def follow(request):
    serializer = CreatefriendSerializer(data=request.data)
    if serializer.is_valid():
        friend = serializer.save()
        messages.success(request, f"The subscription was successful {friend.user} on {friend.userFriend}'s profile")
        return Response({"message": f"The subscription was successful"})
    return Response(serializer.errors, status=400)

