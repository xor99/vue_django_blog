import re
from django.core.paginator import Page
from rest_framework import viewsets

from django.contrib.auth.models import User

from blog_backend import permissions
from blog_backend.models import Article, Tag, Category
from blog_backend.serializers import *
from blog_backend.pagination import ArticlePageNumberPagination

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [permissions.IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return TagListSerializer
        else:
            return TagDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlePerviewSerializer
    permission_classes = [permissions.IsAdminUserOrReadOnly]
    pagination_class = ArticlePageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticlePerviewSerializer
        else:
            return ArticleDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDescSerializer
    permission_classes = [permissions.IsAdminUserOrReadOnly]
