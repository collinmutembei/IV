from api.models.users import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user information"""

    uuid = serializers.UUIDField(read_only=True, format='hex')
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ('uuid', 'username', 'url', 'email', 'password')
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def create(self, validated_data):
        """Modify default method to create user."""
        return User.create_userprofile(**validated_data)
