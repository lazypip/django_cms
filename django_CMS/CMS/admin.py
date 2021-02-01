"""
admin.py为管理模块，admin为模型管理类，使得可以通过后台(web页面形式)直接管理数据库
要继承admin类创建新的模块(数据表)管理类
admin通过models的连接，使数据库的信息返回的web上，同时通过views、models管理数据库
只是一个通过web形式实现可视化管理的方法
"""
from django.contrib import admin
# Register your models here.
from CMS.models import CMS_user


# 创建模型管理类
class UserAdmin(admin.ModelAdmin):
    pass


# 后台管理与数据表映射，将【模型类(数据表)】与【模型管理类】【注册】到admin
admin.site.register(CMS_user, UserAdmin)
