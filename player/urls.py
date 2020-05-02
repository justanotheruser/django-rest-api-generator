from django.urls import path

from .views import ArtistView, SingleArtistView, AlbumView, SingleAlbumView

urlpatterns = [
    path('artist/', ArtistView.as_view()),
    path('artist/<int:pk>/', SingleArtistView.as_view()),
    path('album/', AlbumView.as_view()),
    path('album/<int:pk>/', SingleAlbumView.as_view()),
]