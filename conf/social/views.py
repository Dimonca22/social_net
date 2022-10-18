from .models import *
from .serializers import PostSerializer
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

def register(request):
    return render (request, 'templates/register.html')


def login(request):
    return render (request, 'templates/login.html')


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
