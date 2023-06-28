from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from postsUsers.serializers import * 
 
from friends.models import CreateFriend

@api_view(['GET'])
def friendsPostsSorter(request, userId):
    try:
        friends = CreateFriend.objects.filter(user=userId)
        friend_ids = [friend.userFriend.id for friend in friends]
        posts = Post.objects.filter(user__in=friend_ids)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except CreateFriend.DoesNotExist:
        return Response("User not found in friends list.")
