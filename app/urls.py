from django.conf.urls import url
from app.views import landing

urlpatterns = [
    url(r'^$', landing),
]
