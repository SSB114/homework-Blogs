# blogs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count
from .models import BlogPost, Comment, Like
from .forms import BlogPostForm, CommentForm

# ===== 基础功能 =====

def index(request):
    """显示所有博客文章"""
    from django.db.models import Count

    # 获取文章并预取评论数量
    posts = BlogPost.objects.annotate(
        comment_count=Count('comments')
    ).order_by('-date_added')
    
     # 为每篇文章检查当前用户是否已点赞
    for post in posts:
        if request.user.is_authenticated:
            # 已登录用户：检查是否点赞
            try:
                post.user_has_liked = post.user_has_liked(request.user)
            except Exception:
                post.user_has_liked = False
        else:
            # 未登录用户：不可能点赞
            post.user_has_liked = False  
    
      # 计算统计数据
    total_posts = posts.count()

    from django.db.models import Sum
    total_likes = posts.aggregate(total=Sum('likes_count'))['total'] or 0
    total_comments = posts.aggregate(total=Sum('comment_count'))['total'] or 0
    
    context = {
        'posts': posts,
        'total_posts': total_posts,
        'total_likes': total_likes,
        'total_comments': total_comments,
    }
    
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """创建新文章"""
    if request.method != 'POST':
        # 显示空表单
        form = BlogPostForm()
    else:
        # 处理填写好的表单
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            messages.success(request, '文章已发布！')
            return redirect('blogs:index')
    
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """编辑现有文章"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 确保只有文章所有者可以编辑
    if post.owner != request.user:
        messages.error(request, '您无权编辑此文章。')
        return redirect('blogs:index')
    
    if request.method != 'POST':
        # 显示带有原始数据的表单
        form = BlogPostForm(instance=post)
    else:
        # 处理编辑后的表单
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '文章已更新！')
            return redirect('blogs:index')
    
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

# ===== 新增功能：文章详情、点赞、评论 =====

def post_detail(request, post_id):
    """显示单篇文章详情及评论"""
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()  # 获取所有评论
    comment_form = CommentForm()
    
    # 检查当前用户是否已点赞
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.user_has_liked(request.user)
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_has_liked': user_has_liked,
    }
    return render(request, 'blogs/post_detail.html', context)

@login_required
def add_comment(request, post_id):
    """添加评论"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, '评论已发布')
    
    return redirect('blogs:post_detail', post_id=post_id)

@login_required
def toggle_like(request, post_id):
    """点赞/取消点赞"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 检查是否已点赞
    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user,
        defaults={'post': post, 'user': request.user}
    )
    
    if not created:
        # 如果已存在，则取消点赞（删除记录）
        like.delete()
        post.likes_count = max(0, post.likes_count - 1)
        liked = False
        messages.info(request, '已取消点赞')
    else:
        # 新点赞
        post.likes_count += 1
        liked = True
        messages.success(request, '点赞成功')
    
    post.save()
    
    # 如果是AJAX请求，返回JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'likes_count': post.likes_count,
            'liked': liked
        })
    
    return redirect('blogs:post_detail', post_id=post_id)

@login_required
def delete_comment(request, comment_id):
    """删除评论"""
    comment = get_object_or_404(Comment, id=comment_id)
    
    # 只允许评论作者或文章作者删除
    if request.user == comment.author or request.user == comment.post.owner:
        post_id = comment.post.id
        comment.delete()
        messages.success(request, '评论已删除')
        return redirect('blogs:post_detail', post_id=post_id)
    else:
        messages.error(request, '无权删除此评论')
        return redirect('blogs:post_detail', post_id=comment.post.id)
    
