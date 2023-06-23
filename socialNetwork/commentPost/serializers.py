from rest_framework import serializers
from .models import CommentPost

class CommentPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = CommentPost
            fields = '__all__'