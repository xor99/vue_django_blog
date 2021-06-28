from django.contrib import admin

from blog_backend.models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
