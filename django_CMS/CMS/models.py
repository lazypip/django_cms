# 原有模块
from django.db import models

# Create your models here.
# id | username | password


class CMS_user(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=50)  # 即为表头信息
    password = models.CharField(verbose_name="密码", max_length=50)

    class Meta:
        verbose_name = "用户表" # 在admin管理界面会显示
        verbose_name_plural = verbose_name

    def __str__(self):
        show = 'username: '+self.username
        show_ = '             password: '+('*'*len(self.password))
        return show+show_


'''
models 创建
class Codename(models.Model):     #对应一张表
    field1 = models.XXXField(verbose_name="",max_length= ,default="",null=True,blank=True) #对应数据项 后面为附属项
    field2 = ...
    
    #以下为附属说明子类 (附属项) 
    class Meta: # 解决数据表显示问题
        verbose_name = "用户表" # 在admin管理界面会显示
        verbose_name_plural = verbose_name

    def __str__(self): # 解决数据项显示问题 ps: py2用__unicode__
        show = 'username: '+self.username
        show_ = '             password: '+('*'*len(self.password))
        return show+show_

admin页面设置:
(1) 改时区语言
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

1.Field类型(35 min)





2.Field属性(38 min)
primary_key:设置True or False，定义此字段是否为主键
default:设置默认值，可以设置默认的文本、时间、图片、时间等
null:设置True or False,是否允许数据库字段为Null，默认为False
blank:设置True or False，定义是否运行用户不输入，默认为False;若为True，则用户可以不输入此字段
choices:设置该字段的可选值，本字段的值是一个二维元素的元组;元素的第1个值为实际存储的值，
max_length;设置默认长度,
一般在CharField、 TextField、EmailField等文本字段设置
verbose_name:设置该字段的名称，所有字段都可以设置，在Web页面会显示出来(例如将英文显示
upload_to:设置上传路径，ImageField和FileField字段需要设置此参数

3.Meta类属性



4.数据同步 (43min)
makemigrations [appname]
migrate [appname]

'''
