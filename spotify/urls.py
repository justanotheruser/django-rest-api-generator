from django.contrib import admin
from django.urls import include, path
from player.models import Artist, Album, Track
from rest_framework import generics, routers, serializers, viewsets

urlpatterns = [
    path('api/', include('player.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
