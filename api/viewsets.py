from rest_framework import viewsets
from api.models.user import User
from api.models.image import Image
from api.models.phedited import PheditedImage, FinalImage
from api.serializers import (
    UserSerializer,
    ImageSerializer,
    PheditedImageSerializer,
    FinalImageSerializer
)


class UserViewset(viewsets.ModelViewSet):
    """Serializer for the user model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = ('username')


class ImageViewset(viewsets.ModelViewSet):
    """Serializer for the image model
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        """
        creates image under the users upload directory
        or under anonymous upload directory if user is
        is not logged in
        """
        if self.request.user.is_active:
            serializer.save(uploaded_by=self.request.user)
        elif self.request.user.is_anonymous:
            anonymous_user = User.objects.get(username="anonymous")
            serializer.save(uploaded_by=anonymous_user)


class PheditedImageViewset(viewsets.ModelViewSet):
    """Serializer for phedited image(s) model
    """
    queryset = PheditedImage.objects.all()
    serializer_class = PheditedImageSerializer

    def perform_create(self, serializer):
        """
        creates image under the users upload directory slash phedited
        """
        serializer.save(
            original_image=self.request.data.get('original_image_url'),
            phedited_by=self.request.user,
            effects=self.request.data.get('effects')
        )


class FinalImageViewset(viewsets.ModelViewSet):
    """Serializer for final image(s) model
    """
    queryset = FinalImage.objects.all()
    serializer_class = FinalImageSerializer
