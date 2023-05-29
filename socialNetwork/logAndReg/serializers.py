from django.contrib.auth.models import User
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
        
        data['user'] = user
        return data
from django.contrib.auth.models import User
from rest_framework import serializers



class RegisterSerializer(serializers.Serializer):
    AUTH_TYPES = (
        ('google', 'Google'),
        ('apple', 'Apple'),
    )
    auth_type = serializers.ChoiceField(choices=AUTH_TYPES, label='Authentication Type')
    username = serializers.CharField(max_length=150, label='Username')
    email = serializers.EmailField(label='Email')
    password = serializers.CharField(max_length=128, label='Password', write_only=True)
    repeat_password = serializers.CharField(max_length=128, label='Repeat Password', write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        repeat_password = attrs.get('repeat_password')

        if password != repeat_password:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        auth_type = validated_data.get('auth_type')
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)

        return user

