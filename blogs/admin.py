from django.contrib import admin
from .models import BlogPost
# Register your models here.
# 注册 BlogPost 到后台
admin.site.register(BlogPost)