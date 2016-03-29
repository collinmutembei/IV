from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import (
    UserViewset,
    ImageViewset,
    PheditedImageViewset,
    FinalImageViewset
)

router = routers.DefaultRouter()
router.register(r'users',  UserViewset)
router.register(r'images',  ImageViewset)
router.register(r'phedited',  PheditedImageViewset)
router.register(r'saved',  FinalImageViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
