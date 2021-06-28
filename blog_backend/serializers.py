from django.db import models
from django.db.models import fields
from rest_framework import serializers

from django.contrib.auth.models import User
from blog_backend.models import Article, Tag, Category


class UserDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'date_joined',
            'first_name',
            'last_name',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'id',
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'url',
            'title',
            'id',
        ]


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(read_only=True)

    author = UserDescSerializer(read_only=True)

    tags = TagSerializer(many=True)

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticlePerviewSerializer(ArticleBaseSerializer):

    body_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_perview_md()

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class ArticleDetailSerializer(ArticleBaseSerializer):

    body_html = serializers.SerializerMethodField()

    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class ArticleInOtherView(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'id',
            'url',
        ]


class CategoryListSerializer(serializers.ModelSerializer):

    category_articles = ArticleInOtherView(many=True)

    class Meta:
        model = Category
        fields = [
            'url',
            'title',
            'category_articles',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):

    category_articles = ArticleInOtherView(many=True)

    class Meta:
        model = Category
        fields = [
            'title',
            'category_articles',
            'id'
        ]


class TagListSerializer(serializers.ModelSerializer):

    tag_articles = ArticleInOtherView(many=True)

    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'tag_articles',
            'url',
        ]


class TagDetailSerializer(serializers.ModelSerializer):

    tag_articles = ArticleInOtherView(many=True)

    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'tag_articles',
        ]
