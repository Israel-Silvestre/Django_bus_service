from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from church.views import ChurchList

urlpatterns = [
  path('',ChurchList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)