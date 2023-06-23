from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .serializers import * 
from rest_framework.response import Response
from django.contrib import messages

@swagger_auto_schema(method='post', request_body=CommandPostSerializer)
@api_view(['POST'])
def createCommand(request):
    serializer = CommandPostSerializer(data=request.data)
    if serializer.is_valid():
        command = serializer.save()
        messages.success(request, f"New account created: {command.context}")
        return Response({"message": "User successfully registered"})
    return Response(serializer.errors, status=400)
