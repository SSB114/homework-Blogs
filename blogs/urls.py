from django.urls import path
from . import views

# 这行很重要！定义应用命名空间
app_name = 'blogs'

# 这行也很重要！urlpatterns 必须是这个变量名
urlpatterns = [
    # 主页，显示所有文章
    path('', views.index, name='index'),
    # 添加新文章
    path('new_post/', views.new_post, name='new_post'),
    # 编辑文章
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),

    # 新增：文章详情和互动功能
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

]

