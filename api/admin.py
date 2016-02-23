from django.contrib import admin
from api.models.users import UserProfile, User

admin.site.register(UserProfile)
admin.site.register(User)
