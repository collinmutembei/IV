from django.conf.urls import url
from app.views import landing, dashboard

urlpatterns = [
    url(r'^$', landing),
    url(r'^web/', dashboard),
]
