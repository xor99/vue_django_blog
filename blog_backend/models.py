from django.db import models
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField

from markdown import Markdown

# Create your models here.

# 归档


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='归档名')
    created = models.DateTimeField(
        default=timezone.now, verbose_name='创建时间')

    class Meta:
        ordering = ['-created']  # 定义排序
        verbose_name = '归档'
        verbose_name_plural = '归档'

    def __str__(self):
        return self.title

# 标签


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名')  # 标签名
    created = models.DateTimeField(
        default=timezone.now, verbose_name='创建时间')

    class Meta:
        ordering = ['-created']  # 定义排序
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name

# 文章模型


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')  # 文章关联作者
    title = models.CharField(max_length=255, verbose_name='标题')  # 文章标题
    body = MDTextField(verbose_name='文章内容')  # 文章主题，使用MarkDown
    created = models.DateTimeField(
        default=timezone.now, verbose_name='创建时间')  # 文章创建时间
    updated = models.DateTimeField(
        auto_now=True, verbose_name='更新时间')  # 文章更新时间

    # 管理归档
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='归档', related_name='category_articles')

    # 关联标签
    tags = models.ManyToManyField(
        Tag, blank=True, verbose_name='标签', related_name="tag_articles")

    class Meta:
        ordering = ['-created']  # 定义排序
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'

    def __str__(self):
        return self.title

    # 按文章的百分比读取一部分文章转换MD
    def get_perview_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.nl2br'
            ]
        )

        perview_text = self.body.split('\r\n')
        perview_index = round(len(perview_text) * 0.3)
        text, state, count = [], False, 0
        for item in perview_text:
            if count == perview_index:
                break

            if "```" in item:
                state = not state

            if state:
                text.append(item)
            else:
                text.append(item)
                count += 1

        md_body = md.convert("\n".join(text))

        return md_body

    # 整个文章转换MD
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.nl2br',
            ]
        )

        content = self.body  # .replace('\r\n', '\n')

        md_body = md.convert(content)

        return md_body, md.toc
