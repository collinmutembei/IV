from django.contrib import admin
from api.models.users import UserProfile, User
from api.models.images import Image

admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Image)
