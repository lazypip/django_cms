"""django_CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 初始模块
from django.contrib import admin
from django.urls import path

# 引入views函数
from CMS.views import welcome, index, users, index_delete, index_add, index_exclude, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),   # 欢迎页映射

    path('index', index, name='index'),   # 首页映射
    path('index_add', index_add, name='index_add'),
    path('index_delete', index_delete, name='index_delete'),
    path('index_exclude', index_exclude, name="index_exclude"),

    path('users', users, name='users'),  # 列表页映射
    path('logout', logout, name='logout'), # 退出页
]
