### **Django 个人博客系统**

##### **1.项目简介**

这是一个基于 Django 框架开发的全功能个人博客系统。项目完成了《Python编程：从入门到实践》第19章的任务 19-1（基础博客系统） 和 19-5（受保护博客），并在此基础上自主扩展了用户交互功能（点赞、评论）和前端界面美化。



##### **2. 主要功能**

###### 2.1 基础功能（对应任务 19-1）

    功能				描述

文章管理	 	创建、编辑、删除博客文章

首页展示 	 按时间倒序展示所有文章

后台管理		Django Admin 后台管理文章

表单系统		发表新文章和编辑已有文章的表单

###### 2.2 权限控制（对应任务 19-5）

    功能				描述

用户关联		每篇文章关联到特定用户

公开访问		所有文章无需登录即可浏览

发布权限		仅登录用户可发布新文章

编辑权限		仅文章作者可编辑自己的文章

###### 2.3 自主扩展功能

    功能				描述

点赞系统		AJAX 异步点赞/取消点赞，无需刷新页面

评论功能		文章评论区，支持评论删除

统计面板		侧边栏显示文章、点赞、评论总数

界面美化		Bootstrap 5 响应式设计 + 自定义 CSS



##### **3.项目结构**

Blog/                           # 项目根目录

├── blogs/                      # 博客核心应用

│   ├── migrations/             # 数据库迁移文件

│   ├── templates/blogs/        # 博客模板文件

│   │   ├── base.html          # 基础模板

│   │   ├── index.html         # 首页

│   │   ├── post\_detail.html   # 文章详情页

│   │   ├── new\_post.html      # 新建文章页

│   │   └── edit\_post.html     # 编辑文章页

│   ├── \_\_init\_\_.py            # Python包初始化文件

│   ├── admin.py               # 后台管理配置

│   ├── apps.py                # 应用配置

│   ├── forms.py               # 表单定义

│   ├── models.py              # 数据模型 (BlogPost, Comment, Like)

│   ├── tests.py               # 测试文件

│   ├── urls.py                # 应用路由

│   └── views.py               # 视图函数

├── accounts/                   # 用户认证应用

│   ├── templates/accounts/     # 认证模板

│   │   ├── login.html         # 登录页面

│   │   └── register.html      # 注册页面

│   ├── \_\_init\_\_.py

│   ├── admin.py

│   ├── apps.py

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── Blog/                       # Django项目设置目录

│   ├── \_\_init\_\_.py

│   ├── asgi.py                # ASGI配置

│   ├── settings.py            # 项目设置

│   ├── urls.py                # 项目主路由

│   └── wsgi.py                # WSGI配置

├── static/                     # 静态文件 (CSS, JS, 图片)

├── media/                      # 用户上传文件

├── db.sqlite3                  # SQLite 数据库

├── manage.py                   # Django 管理脚本

└── requirements.txt            # 项目依赖



##### **4.操作步骤**

###### 1）克隆项目

git clone https://github.com/Hyacine5207/hyacine4.git

cd hyacine4

###### 2）设置虚拟环境

\# 创建虚拟环境

python -m venv blog\_env



\# 激活虚拟环境

\# Windows:

blog\_env\\Scripts\\activate

\# Mac/Linux:

source blog\_env/bin/activate

###### 3）安装依赖

pip install django

###### 4）数据库迁移

\# 应用数据库迁移

python manage.py migrate



\# 创建超级用户（用于后台管理）

python manage.py createsuperuser

\# 按提示输入用户名、邮箱和密码

###### 5）运行开发服务器

\# 启动开发服务器

python manage.py runserver



\# 服务器启动后，访问以下地址：

\# - 首页：**http://127.0.0.1:8000/**

\# - 后台管理：**http://127.0.0.1:8000/admin/**



##### **5.功能使用指南**

###### 用户注册与登录

1.访问首页，点击右上角 "注册" 链接

2.填写用户名、邮箱和密码创建账户

3.使用注册的账户登录系统



###### 发布新文章

1.登录后，点击首页右上角 "写新文章" 按钮

2.填写文章标题和内容

3.点击 "发布" 按钮提交



###### 编辑已有文章

1.在首页或文章详情页，找到自己发布的文章

2.点击 "编辑" 按钮（仅自己的文章显示此按钮）

3.修改文章内容后保存

###### 

###### 点赞与评论

1.点赞：在文章卡片下方点击 "点赞" 按钮（异步更新，无需刷新页面）

2.评论：在文章详情页底部评论区发表评论

3.删除评论：文章作者可删除任意评论，评论者只能删除自己的评论



开发时间：2025年12月

课程：Python 课程实验

作者：刘浩翔

GitHub: https://github.com/Hyacine5207/hyacine4



提示：如果在使用过程中遇到问题，请先检查虚拟环境是否激活，以及所有迁移是否已正确应用。

