from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet

app_name = 'blog'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
