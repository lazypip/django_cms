# django_cms

#### 写的第一个djanco_cms项目，实现了基本的数据管理操作，下面是一些自己总结的框架学习中的小tips，分享给大家

#### 一.  virtualenv （进阶:wrapper版)
    
     创建虚拟目录，实现项目之间环境隔离，解决不同拓展包的版本冲突。虚拟路径就是拷贝物理路径基础文件包到一个独立的包，这样方便管理每个项目所需的特定拓展包，不至于全部堆在一起。
	pip install 
	virtualenv ...    #创建虚拟环境目录
	cd .../Scripts  #进入目录
	dir #查看目录
	activate.bat 激活并进入当前虚拟环境
	pip list  /  python
	deactivate.bat  退出当前环境
                 在虚拟目录下安装django模块

##### ps: 
      在做一个项目的时候一定要保证在虚拟环境的cmd下操作      
      下载中断报错时更换国内的源
      script 脚本 Lib 库
      下载的包一般会安装到Lib中的site-packages
      环境变量原理：执行一个指定程序


#### 二. mysql-python驱动

     py为数据库提供了api。一般pip install pymysql(对于python 3 2用mysqldb)，可用import pymysql测试。mysql默认端口3306，注意xampp与本机数据库同时安装造成的服务冲突(注册表)，一般数据库服务开一个就够了。(xampp msi安装 软件包配置)
  

#### 三. 使用Navicat连接数据库

    配置mysql，可用msi/软件包/集成环境，并用Navicat直接安装即可。开启数据库服务后连接数据库。

#### 四. pycharm创建项目
  
        注意是使用现有的ven环境而不是 new ven。由于django里面默认的是MySQLdb，所以要在__init__.py模块里加入以下内容：
	import pymysql
	pymysql.install_as_MySQLdb()	

##### 代码格式矫正:

	# 后加一个空格
	,后加一个空格
	pycharm建议用小写与下划线拼凑变量名，常量用大写
	最后一行为空行
	逻辑、原理性知识：


#### 五.原生文件架构作用 :

	__init__.py : 让py把该目录当成一组模块所需的文件(默认为空)
	urls.py :       网址映射，将用户输入的url映射到后台逻辑视图
	settings.py :全局系统参数设置
	manage.py :django命令行管理工具，用于启动服务(run stop操作本质)、数据库同步、创建管理员等系统管理
	templates :  放置web静态文件，即html文件
	wsgi.py :      定义WSGI接口，用于与Web服务器联动。(django自带小的数据库与服务器做测试用)
	安全性:  自带安全措施，加入安全代码

# 【目标项目描述】
##### 项目名称：

     DjangoCMS用户信息管理系统
   
##### 项目需求：

1.用户欢迎页 welcome.html
   要求：能够跳转至主页...

2.用户管理主页 index.html
   要求：提交、查询、删除...

3.用户列表页 list.html
   要求：列出网站提交过的用户信息...


##### 项目部署：

1.新建app应用

	运行manager.py
	startapp CMS , 创建框架
2.页面实现

	(1)前端部分:
	template构建html页面(构建html页面、配合views中的动态操作)，设置好页面关联信息，结合需求设计出动态框架get post按钮，从而写出待渲染部分{% %}。并作为views函数的编写指南	

	(2)数据库部分:
	mysql中创建新数据库utf8 utf8_general_ci防止乱码。
	models数据库联动部分，setting中对app进行注册后，设置目标数据库信息，进行数据迁移(makemig...  migrate)。根据需要在models中继承类并建立数据表（一个或多个）与表单信息，再迁移一次。
	

	(3)服务器部分:
	views编写函数，进行页面渲染与返回(进行动态操作，数据库联动、各类语法与返回html页面的方法)，要导入返回方法与数据表单信息。做好从前端与后端的连接。
	urls建立映射(建立url与views函数映射，name属性为url名与函数名、html名区分开)，要导入views函数

3.admin后台操作:

	创建并注册模块管理类 admin.py
	创建admin超级用户 createsuperuser
	登录后台，通过model附属函数装饰后台页面
 
 
 4.admin原理：
  
      admin.py为管理模块，admin为模型管理类，使得可以通过后台(web页面形式)直接管理数据库。要继承admin类创建新的模块(数据表)管理类。admin通过models的连接，使数据库的信息返回的web上，同时通过views、models管理数据库，只是一个通过web形式实现可视化管理的方法


##### 原理简述:

	          HttpRequst-> urls ->views ->HttpResponse HTML ->web browser
	path函数部分原型 path(route, views, name)
	GET请求特定网页时，通过urls转到views函数，在views函数中先调用models联系数据库，对html进行渲染后返回指定网页。即通过接收请求的页面route属性到函数。
	POST请求，html的表单对应一个urls(html指定的)，执行函数内容。即通过name属性来到函数。也是先调用models联系数据库，再对html进行渲染后返回指定页面
	ps: views函数的返回值为函数，所以返回/渲染页面的时候也是执行了一个函数
	其他动作，在html中将一个按钮对应到urls，从而执行函数


##### 其他高级用法:


1. 模式页面中的拓展
2. urls映射用正则实现
3. 高级映射方法：
	反向url映射 name=""
	带命名参数的url映射
	分布式url映射
	多目录映射(目录式映射)
4. httpresponse的其他返回方法
5. 基于类的view函数写法
6. 模板接收模板变量原理(在users函数处) 通过render(渲染)函数   回去 再用for if。拓展模板语言的语法 即渲染语法
7. template模板继承语法
