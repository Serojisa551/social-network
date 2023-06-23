from rest_framework import serializers
from .models import CommandPost

class CommandPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = CommandPost
            fields = '__all__'

    # postId = serializers.IntegerField()
    # username = serializers.CharField()
    # context = serializers.CharField()

    # def create(self, validated_data):
    #     post = validated_data.get("post")
    #     user = validated_data.get("user")
    #     context = validated_data.get("context")

    #     if not postId:
    #         raise serializers.ValidationError("postid field is required.")

    #     if not username:
    #         raise serializers.ValidationError("username field is required.")

    #     if not context:
    #         raise serializers.ValidationError("context field is required.")

    #     command = CommandPost.objects.create(postId=postId, user=user, context=context)
    #     return command