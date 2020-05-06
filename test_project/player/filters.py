import django_filters

from player.models import Artist, Album


class AlbumFilter(django_filters.FilterSet):
    make = django_filters.ModelChoiceFilter(field_name ="artistid",
                                            queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = ('artist',)