from api.viewsets import UserViewset, ImageViewset, PheditedImageViewset
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',  UserViewset)
router.register(r'images',  ImageViewset)
router.register(r'phedited',  PheditedImageViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
