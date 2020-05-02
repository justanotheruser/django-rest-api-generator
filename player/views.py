from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from player.models import Artist, Album, Track
from player.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from player.filters import AlbumFilter

class ArtistView(ListModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            artist_saved = serializer.save()
        return Response({'pk': format(artist_saved.pk)}, status=201)

    def put(self, request, pk):
        artist = get_object_or_404(Artist.objects.all(), pk=pk)
        serializer = ArtistSerializer(
            instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            artist_saved = serializer.save()
        return Response({})

    def delete(self, request, pk):
        artist = get_object_or_404(Artist.objects.all(), pk=pk)
        artist.delete()
        return Response({}, status=204)


class SingleArtistView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class AlbumView(ListModelMixin, GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({'pk': format(album_saved.pk)}, status=201)

    def put(self, request, pk):
        album = get_object_or_404(Album.objects.all(), pk=pk)
        serializer = AlbumSerializer(
            instance=album, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({})

    def delete(self, request, pk):
        album = get_object_or_404(Album.objects.all(), pk=pk)
        album.delete()
        return Response({}, status=204)


class SingleAlbumView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class TrackView(ListModelMixin, GenericAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            track_saved = serializer.save()
        return Response({'pk': format(track_saved.pk)}, status=201)

    def put(self, request, pk):
        track = get_object_or_404(Track.objects.all(), pk=pk)
        serializer = TrackSerializer(
            instance=track, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            track_saved = serializer.save()
        return Response({})

    def delete(self, request, pk):
        track = get_object_or_404(Track.objects.all(), pk=pk)
        track.delete()
        return Response({}, status=204)


class SingleTrackView(RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
