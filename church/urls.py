from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from church import views

urlpatterns = [
  path(r'', views.church_index),
]

urlpatterns = format_suffix_patterns(urlpatterns)