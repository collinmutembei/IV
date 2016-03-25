from api.models.user import User
from api.models.image import Image
from api.models.phedited import PheditedImage
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user information
    """

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
        """creates a user
        """

        user = User(
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for images
    """

    image = serializers.ImageField(use_url=True)
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')

    class Meta:
        model = Image
        fields = ('id', 'image', 'uploaded_by', 'created_at', 'updated_at')


class PheditedImageSerializer(serializers.ModelSerializer):
    """Serializer for phedited images
    """

    original_image = serializers.URLField(
        allow_blank=False,
        read_only=True
    )
    phedited_image = serializers.ImageField(use_url=True, read_only=True)
    phedited_by = serializers.ReadOnlyField(source='uploaded_by.username')
    effects = serializers.CharField(read_only=True)

    class Meta:
        model = PheditedImage
        fields = (
            'original_image',
            'phedited_image',
            'phedited_by',
            'phedited_at',
            'effects'
        )
