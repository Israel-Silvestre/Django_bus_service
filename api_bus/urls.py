
 

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('church/', include('church.urls')),
    path('member/', include('member.urls')),
    path('bus/', include('bus.urls')),
    path('admin/', admin.site.urls),
]