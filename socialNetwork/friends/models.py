from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    userFriend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userFriend")

    class Meta:
        unique_together = ('user', 'userFriend')

    # def d(self, arr):
    #     print(arr)
    #     user = arr.get("user")
    #     userFriend = arr.get("userFriend")
    #     print("self.user", user)
    #     print("self.userFriend", userFriend)

    #     print("type.self.user", type(user) )
    #     print("type.self.userFriend", type(userFriend))


        