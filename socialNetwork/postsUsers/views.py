from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@swagger_auto_schema(method='post', request_body=PostSerializer)
@api_view(['POST'])
def postsUsers(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        # print("serializer.validated_data", serializer.validated_data)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)