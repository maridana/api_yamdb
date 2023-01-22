from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserCreateView, UserReceiveTokenViewSet, UserViewSet

v1_router = DefaultRouter()

v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path(
        'v1/auth/signup/',
        UserCreateView.as_view(),
        name='signup'
    ),
    path(
        'v1/auth/token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]
