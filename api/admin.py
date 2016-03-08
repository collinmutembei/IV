from django.contrib import admin
from api.models.user import User
from api.models.image import Image
from api.models.phedited import PheditedImage

admin.site.register(User)
admin.site.register(Image)
admin.site.register(PheditedImage)
