from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .serializers import * 
from rest_framework.response import Response
from django.contrib import messages

@swagger_auto_schema(method='post', request_body=CommentPostSerializer)
@api_view(['POST'])
def createComment(request):
    serializer = CommentPostSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.save()
        messages.success(request, f"New comment for posts created: {comment.context}")
        return Response({"message": "New comment for posts created"})
    return Response(serializer.errors, status=400)
