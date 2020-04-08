from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', obtain_auth_token),
]