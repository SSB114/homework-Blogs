# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # 使用 Django 内置的登录视图
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # 使用 Django 内置的登出视图
    path('logout/', auth_views.LogoutView.as_view(next_page='blogs:index'), name='logout'),
    
    # 注册视图需要自定义
    path('register/', views.register, name='register'),
]