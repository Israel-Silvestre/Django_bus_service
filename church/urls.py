from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from church import views

urlpatterns = [
  path('', views.ChurchList.as_view()),
  path('<str:id>/list_members', views.get_members)
]

urlpatterns = format_suffix_patterns(urlpatterns)