from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from logAndReg.serializers import RegisterSerializer


# serializer.py
class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    photo = serializers.ImageField(allow_empty_file=True, required=False)
    video = serializers.FileField(allow_empty_file=True, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    location = serializers.CharField(allow_blank=True, required=False)
    url = serializers.URLField(allow_blank=True, required=False)
    


    class Meta:
        model = Post
        fields = ('user', 'photo', 'video', 'description', 'location', 'url')
    # def validate(self, attrs):'user_id' ,
    #     photo = attrs.get("photo")
    #     video = attrs.get("video")

    #     if not (photo or video): 
    #         raise serializers.ValidationError("There must be at least one photo or video")
        
    #     return attrs
    
    def create(self, validated_data):
        user_data = next(iter(validated_data.items()))
        validated_data.popitem(last=False)
        # print("user_data", user_data)
        users = user_data[1]
        # print("users", users) 
        # 
        # print("user_data", user_name)

        # if not user_data:
        #     raise serializers.ValidationError("user field is required.")

       
        # if not user_name:
        #     raise serializers.ValidationError("user username is required.")
        
        usr = User.objects.get(username=users)
        # print("user_data", user)
        post = Post.objects.create(user=usr, **validated_data)

        return post     

        


