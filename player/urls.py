from django.urls import path

from .views import ArtistView, SingleArtistView

urlpatterns = [
    path('artist/', ArtistView.as_view()),
    path('artist/<int:pk>/', SingleArtistView.as_view()),
]