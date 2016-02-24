from api.models.users import UserProfile
from api.models.images import Image
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
    avater_url = serializers.ReadOnlyField()

    class Meta:
        model = UserProfile
        fields = ('uuid', 'username', 'url', 'email', 'password', 'avater_url')
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def create(self, validated_data):
        """Modify default method to create user."""
        return User.create_userprofile(**validated_data)


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for images"""

    image = serializers.ImageField(use_url=True)
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')

    class Meta:
        model = Image
        fields = ('image', 'uploaded_by', 'created_at', 'updated_at')
