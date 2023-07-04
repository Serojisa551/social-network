from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def sortPostsByTime(request):
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sortByPostsPopularity(request):
    posts = Post.objects.all().order_by('-good')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)