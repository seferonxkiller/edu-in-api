from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response
from .serializers import PostDetailSerializer, PostSerializer, BodySerializer, CommentSerializer
from .models import Post, Body, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostSerializer
        return PostDetailSerializer


class BodyRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer


class CommentListCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(parent_comment__isnull=True)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['post_id'] = self.kwargs.get('post_id')
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.kwargs.get('post_id')
        qs = qs.filter(post_id=post_id)
        return qs