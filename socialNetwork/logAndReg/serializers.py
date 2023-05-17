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
