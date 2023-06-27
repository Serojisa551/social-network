from rest_framework import serializers
from .models import CreateFriend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreatefriendSerializer(serializers.ModelSerializer):
        class Meta:
            model = CreateFriend
            fields = ["user", "userFriend"]

        def create(self, arr):
            username = arr.get("user")
            userFriendName = arr.get("userFriend")
            print("type(username)", type(username))
            if username == userFriendName:
                raise ValidationError("User cannot friend the yourself")
            user = User.objects.get(username=username)
            userFriend = User.objects.get(username=userFriendName)
            friend = CreateFriend.objects.create(user=user, userFriend=userFriend)
            return friend