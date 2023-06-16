from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from logAndReg.serializers import RegisterSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
