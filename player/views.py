from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from .models import Artist
from .serializers import ArtistSerializer


class ArtistView(ListModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = ['name']
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
        artist = get_object_or_404(Article.objects.all(), pk=pk)
        artist.delete()
        return Response({}, status=204)


class SingleArtistView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']