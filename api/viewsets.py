from api.models.users import UserProfile
from api.models.images import Image
from api.serializers import UserSerializer, ImageSerializer
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response


class UserlistViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = ('username')

    def create(self, request):
        """Define customizations during user creation."""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                UserProfile.create_userprofile(**serializer.validated_data)
                return Response({
                    'message': 'user created'
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({
                    'message': 'user with entered email already exists'
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': "user not created"
        }, status=status.HTTP_400_BAD_REQUEST)


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        if self.request.user.is_active:
            serializer.save(uploaded_by=self.request.user.profile)
        elif self.request.user.is_anonymous:
            anonymous_user = UserProfile.objects.get(username="anonymous")
            serializer.save(uploaded_by=anonymous_user)
