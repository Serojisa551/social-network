from rest_framework import serializers
from .models import  Message#ChatUser,
from django.contrib.auth.models import User
from rest_framework import serializers

# class ChatUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatUser
#         fields = '__all__' 

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.name', read_only=True)
    recipient_name = serializers.CharField(source='recipient.name', read_only=True)

    class Meta:
        model = Message
        fields = ['sender_name', 'recipient_name', 'content']

    def create(self, validated_data):
        sender_data = validated_data.pop('sender', None)
        if not sender_data:
            raise serializers.ValidationError("Sender field is required.")

        sender_name = sender_data.get('name')
        if not sender_name:
            raise serializers.ValidationError("Sender name is required.")

        recipient_name = validated_data.pop('recipient')['name']
        sender = User.objects.get(name=sender_name)
        recipient = User.objects.get(name=recipient_name)
        message = Message.objects.create(sender=sender, recipient=recipient, **validated_data)
        return message


