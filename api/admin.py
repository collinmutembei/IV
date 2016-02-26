from django.contrib import admin
from api.models.user import User
from api.models.image import Image

admin.site.register(User)
admin.site.register(Image)
