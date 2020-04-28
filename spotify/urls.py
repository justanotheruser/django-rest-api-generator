from django.contrib import admin
from django.urls import include, path
from player.models import Artist, Album, Track
from rest_framework import routers, serializers, viewsets

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['pk', 'name']

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['pk', 'title', 'release_date', 'artist']

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['pk', 'title', 'length', 'album', 'artist']

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

router = routers.SimpleRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('player/', include('player.urls')),
    path('admin/', admin.site.urls),
]
