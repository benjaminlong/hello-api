from rest_framework import serializers

from django.contrib.auth import get_user_model
from hello_api.users.models import User


class SimpleUserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk"]


class ReadeUserSerializer():
    pass


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["pk", "username", "email", "first_name"]

        # fields = ["username", "email", "name", "url"]
        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        # }
