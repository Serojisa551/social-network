from .models import UserInfo
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import secrets
import string

# This shouldn't work with Swagger It's token generation that is called during registration
def generateToken():
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(16))
    return token



class AuthorisationSerializer(serializers.Serializer):
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



class AuthenticationTypeSerializer(serializers.Serializer):
    AUTH_TYPES = (
        ('google', 'Google'),
        ('apple', 'Apple'),
        ('web', 'Web')
    )


class RegisterSerializer(serializers.Serializer):
    auth_type = serializers.ChoiceField(choices=AuthenticationTypeSerializer.AUTH_TYPES, label='Authentication Type')
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField(required=False)
    date_of_birth = serializers.DateField(required=False)
    place_of_birth = serializers.CharField(required=False)

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
        token = generateToken()
        

        if auth_type == "web":
            # profile_picture = validated_data.get('profile_picture')
            date_of_birth = validated_data.get('date_of_birth')
            place_of_birth  = validated_data.get('place_of_birth')
            userInfo = UserInfo.objects.create_user(username=username, date_of_birth=date_of_birth, place_of_birth=place_of_birth, token=token)
            user = User.objects.create_user(username=username, email=email, password=password)
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            userInfo = UserInfo.objects.create_user(username=username, token=token)

        return user, userInfo

