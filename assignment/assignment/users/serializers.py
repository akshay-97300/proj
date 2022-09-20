from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    user serializer
    """
    class Meta:
        """
        Meta class define for a User Model..
        """
        model = User
        fields = "__all__"

