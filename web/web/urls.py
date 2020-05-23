from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^wm/', include('wm.urls')),
    url(r'^admin/', admin.site.urls),
]