# blogs/forms.py
from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']  # 字段名应该是content，不是text
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': '写下你的文章内容...'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': '写下你的评论...',
                'class': 'form-control'
            })
        }
        labels = {
            'content': ''
        }