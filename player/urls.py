from django.urls import path

from player.views import ArtistView, AlbumView, TrackView
from player.views import SingleArtistView, SingleAlbumView, SingleTrackView

urlpatterns = [
    path('artist/', ArtistView.as_view()),
    path('artist/<int:pk>/', SingleArtistView.as_view()),
    path('album/', AlbumView.as_view()),
    path('album/<int:pk>/', SingleAlbumView.as_view()),
    path('track/', TrackView.as_view()),
    path('track/<int:pk>/', SingleTrackView.as_view()),
]
