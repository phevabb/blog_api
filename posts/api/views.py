from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from posts.api.serializers import PostSerializer
from posts.models import Post
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):


    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

