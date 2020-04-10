from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register('v1/posts', PostViewSet)
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, 'post_id')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]
