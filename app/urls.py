from django.conf.urls import url
from app.views import landing, dashboard, applyeffects

urlpatterns = [
    url(r'^$', landing),
    url(r'^web/', dashboard),
    url(r'^effects/', applyeffects.as_view()),
]
