from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('church/', include('church.urls')),
    path('member/', include('member.urls')),
    path('member_church/', include('member_church.urls')),
    path('bus/', include('bus.urls')),
    path('admin/', admin.site.urls),
]