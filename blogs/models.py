# blogs/models.py
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 新增：点赞计数
    likes_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    # 检查用户是否已点赞
    def user_has_liked(self, user):
        if not user.is_authenticated:
            return False
        if not hasattr(user, 'id') or user.id is None:
            return False
        return self.likes.filter(user=user).exists()

class Comment(models.Model):
    """评论模型"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # 按时间倒序排列
    
    def __str__(self):
        return f'评论 by {self.author} on {self.post}'

class Like(models.Model):
    """点赞模型"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # 确保每个用户对每篇文章只能点赞一次
        unique_together = ['post', 'user']
    
    def __str__(self):
        return f'{self.user} 点赞了 {self.post}'