from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AdminViewSet, SignUpView, TokenView, UsersView

router = DefaultRouter()
router.register('users', AdminViewSet, basename='users')

urlpatterns = [
    path('v1/users/me/', UsersView.as_view(), name='users'),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', TokenView.as_view(), name='token'),
    path('v1/', include(router.urls)),
]
