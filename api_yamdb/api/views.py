from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from reviews.models import Review
from titles.models import Category, Genre, Title

from .filters import TitleFilter
from .mixins import ListCreateDeleteViewSet
from .permissions import (AdminOrReadOnlyPermission,
                          IsAuthOrAdmionOrModeratorOrReadOnly)
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer, TitleSerializer)


class GenreViewSet(ListCreateDeleteViewSet):
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    search_fields = ('name',)
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminOrReadOnlyPermission,)


class CategoryViewSet(ListCreateDeleteViewSet):
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    queryset = Category.objects.all()
    search_fields = ('name',)
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminOrReadOnlyPermission,)


class TitleViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    permission_classes = (AdminOrReadOnlyPermission,)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthOrAdmionOrModeratorOrReadOnly]

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return serializer.save(
            author=self.request.user,
            title=title,
        )

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthOrAdmionOrModeratorOrReadOnly]

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id')
        )
        return serializer.save(
            author=self.request.user,
            review=review,
        )

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )
        return review.comments.all()
