from django.contrib import admin
from .models import Article
# Register your models here.

# 어드민에 Article model 등록
admin.site.register(Article)