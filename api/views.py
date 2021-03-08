from rest_framework import viewsets
from rest_framework import permissions

from users.models import CustomUser
from articles.models import Article

from .serializers import (
                        CustomUserSerializer,
                        ArticleSerializer,
                        ArticleDetailSerializer,
                        CustomUserDetailSerializer
                        )


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CustomUserDetailSerializer
        return CustomUserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleSerializer
