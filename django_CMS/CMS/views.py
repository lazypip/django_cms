# 以下为返回 html页面方法(附用法)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# return render(request,"welcome.html",{}) "渲染" html页面进行返回
# return HttpResponse("html内容")   直接返回""中的html代码
# return HttpResponseRedirect(reverse("users"))   重定向
'''
重定向原理简介:
HttpReponseDirect只支持hard coded urls(硬编码链接), 不能直接使用命名的URL，如使用HttpResponseDirect('blog:article_list‘)是错误的。在使用URL命名时，我们需要先通过URL反向解析方法reverse先对命名URL(article_list)进行解析，然后再使用HttpReponseRedirect定向(如下面的代码)。背后的逻辑是reverse('blog:article_list')='/index/'。
'''

# 以下为数据库表单
from CMS.models import CMS_user

# Create your views here.


def welcome(request):
    return render(request, "welcome.html", {})


def index(request):
    return render(request, "index.html", {})


def index_add(request):
    if request.method == "POST":
        username = request.POST.get("username", "")  # username是post变量名
        password = request.POST.get("password", "")
        usermsg = CMS_user()         # 创建一个id项(对象)并赋值
        usermsg.username = username
        usermsg.password = password
        usermsg.save()
        return HttpResponseRedirect(reverse("users"))
    else:
        return HttpResponse("<h1>404 NOT FOUND</h1>")


def index_delete(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        deluser = CMS_user.objects.filter(username=username, password=password)  # 指定(过滤出)一个id项
        deluser.delete()
        return HttpResponseRedirect(reverse('users'))
    # 由于只是index的附属品，只是添加一个post接收方法，所以可以不设get请求返回页面
    # 也可以先访问此空白页然后POST请求
    else:
        return HttpResponse("<h1>404 NOT FOUND</h1>")


def index_exclude(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        excluder = CMS_user.objects.exclude(username=username, password=password) # 类.objects指示一个表的信息
        excluder.delete()
        return HttpResponseRedirect(reverse('users'))
    else:
        return HttpResponse("<h1>404 NOT FOUND</h1>")


def users(request):
    all_user = CMS_user.objects.all()  # 模板变量 读取数据库全部信息并赋值给all_user
    # 与user.html相互联动   all_user可在html中使用
    # 通过模板变量传递给template的 html页面
    # 模板就有权力使用左边的all_user
    return render(request, "users.html", {"all_user": all_user})


def logout(request):
    return render(request, 'logout.html', {})


def sample(request):
    # 以下方法均可混用拼凑成高级用法
    # 查询/赋值信息(从数据库导出数据) objects即对象，指示数据库的id
    data = CMS_user.objects.all()      # 查询模型类的所有数据
    data = CMS_user.objects.flter()   # 返回符合筛选条件的数据集(一个或多个对象)
    data = CMS_user.objects.get()    # 返回符合筛选条件的数据(单个对象)
    data = CMS_user.objects.exclude()  # 返回不符合筛选条件的数据集

    '''增加删除需要先指定数据项'''
    tmp = CMS_user()  # 创建一个id项并赋值
    tmp.username = "123"
    tmp.password = "123"

    # 增加
    tmp.save()
    tmp.objects.create(username="123", password="123")

    # 删除
    '''先查询指定了id项再delete data = ...'''
    data.delete()

    # 排序
    data = CMS_user.objects.all().order_by("username")  # 查询所有数据并按照关键字排序

    # 切片
    data = CMS_user.objects.all().order_by("username")[:1:]
