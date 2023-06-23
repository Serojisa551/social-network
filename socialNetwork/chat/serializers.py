from rest_framework import serializers
from .models import  Message
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source="sender.username")
    recipient_name = serializers.CharField(source="recipient.username")

    class Meta:
        model = Message
        fields = ["sender_name","recipient_name", "content"]

    def create(self, validated_data):
        sender_data = validated_data.pop("sender", None)
        if not sender_data:
            raise serializers.ValidationError("Sender field is required. I too.")

        sender_name = sender_data.get("username")
        if not sender_name:
            raise serializers.ValidationError("Sender username is required.")

        recipient_name = validated_data.pop("recipient")["username"]
        sender = User.objects.get(username=sender_name)
        recipient = User.objects.get(username=recipient_name)
        message = Message.objects.create(sender=sender, recipient=recipient, **validated_data)
        return message


