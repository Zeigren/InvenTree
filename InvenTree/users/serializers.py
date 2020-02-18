from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for a User
    """

    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "first_name",
            "last_name",
            "email",
        )
