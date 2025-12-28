from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录
            login(request, new_user)
            return redirect('blogs:index')  # 重定向到首页
    
    # 显示空表单或指出表单无效
    context = {'form': form}
    return render(request, 'accounts/register.html', context)