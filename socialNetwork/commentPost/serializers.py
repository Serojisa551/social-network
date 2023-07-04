from rest_framework import serializers
from .models import CommentPost
from postsUsers.models import Post

class RatingTypeSerializer(serializers.ModelSerializer):
    RATING_TYPES = (
        ("good", "GOOD"),
        ("norm","NORM"),
        ("bad","BAD")
        )
        
class CommentPostSerializer(serializers.ModelSerializer):
    rating = serializers.ChoiceField(choices=RatingTypeSerializer.RATING_TYPES, label="RATING Type",  required=False)
    
    class Meta:
        model = CommentPost
        fields =  ["userId", "postId", "context", "rating"]
        

    def create(self, validated_data):
        rating = validated_data.pop("rating", None)
        userId = validated_data.get("userId")
        postId = validated_data.get("postId")
        context = validated_data.get("context")  
        if rating == "good":
            postId.getGood()
        elif rating == "norm":
            postId.getNorm()
            print("norm", postId.norm)
        elif rating == "bad":
            postId.getBad()
            print("bad", postId.bad)
        comment = CommentPost.objects.create(userId=userId, postId=postId, context=context)
        
        return comment