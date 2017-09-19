from django.conf.urls import url
from app.views import landing, dashboard, gallery, cssgrid

urlpatterns = [
    url(r'^$', landing),
    url(r'^app/', dashboard),
    url(r'^gallery/', gallery),
    url(r'^css/', cssgrid),
]
