import django_filters
from django_filters.rest_framework import filters

from titles.models import Title


class TitleFilter(django_filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='iexact'
    )
    genre = django_filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='iexact'
    )

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')
