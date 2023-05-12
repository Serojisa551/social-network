from django.contrib.auth.models import User
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class CreateUserSerializer(serializers.ModelSerializer):

    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repeat_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        repeat_password = validated_data.pop('repeat_password')
        if validated_data['password'] != repeat_password:
            raise serializers.ValidationError("Passwords do not match.")
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password',]
        extra_kwargs = {'password': {'write_only': True}}

    def login(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['password'],
            
        )
        return  user