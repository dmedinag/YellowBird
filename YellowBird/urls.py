from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^bot/', include('bot.urls')),
    url(r'^admin/', admin.site.urls),
]