from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def clap(self, request, pk=None):
        blog = self.get_object()
        blog.claps += 1
        blog.save()
        return Response({'claps': blog.claps})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_id = self.request.data.get('blog')
        blog = Blog.objects.get(pk=blog_id)
        serializer.save(author=self.request.user, blog=blog)
