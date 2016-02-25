from api.models.user import User
from api.models.image import Image
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user information"""

    uuid = serializers.UUIDField(read_only=True, format='hex')
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ('uuid', 'username', 'url', 'password')
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def create(self, validated_data):

        user = User(
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for images"""

    image = serializers.ImageField(use_url=True)
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')

    class Meta:
        model = Image
        fields = ('image', 'uploaded_by', 'created_at', 'updated_at')
