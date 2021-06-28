from rest_framework.pagination import PageNumberPagination


class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 3
