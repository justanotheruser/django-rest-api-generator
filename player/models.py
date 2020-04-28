from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)


class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Track(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveSmallIntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
