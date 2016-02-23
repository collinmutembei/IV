from api.models.users import UserProfile
from api.serializers import UserSerializer
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
