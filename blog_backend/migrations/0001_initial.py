# Generated by Django 3.2.4 on 2021-06-23 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='归档名')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '归档',
                'verbose_name_plural': '归档',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='文章内容')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_articles', to='blog_backend.category', verbose_name='归档')),
                ('tags', models.ManyToManyField(blank=True, related_name='tag_articles', to='blog_backend.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
                'ordering': ['-created'],
            },
        ),
    ]