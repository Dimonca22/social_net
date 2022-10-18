from .models import *
from .serializers import PostSerializer
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
