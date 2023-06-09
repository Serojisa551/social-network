from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.serializers import ValidationError



class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



