from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

app_name: str = 'api'

router = DefaultRouter()

router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    'reviews'
)
router.register(
    (r'titles/(?P<title_id>\d+)'
     r'/reviews/(?P<review_id>\d+)/comments'),
    CommentViewSet,
    'comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
