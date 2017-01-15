from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('www.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
