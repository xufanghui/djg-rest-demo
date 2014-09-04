安装及测试demo的说明
1.安装及测试环境
  1.安装环境为virtual box 4.2.12 
  2.虚拟机系统为debian 7.1 wheely 64bit
  3.数据库为POSTGRESQL 9.1
  4.编程语言：python 2.7.5 
  5.编程语言依赖的库：
          1.Django-1.6.6
            官方网址： https://www.djangoproject.com
          2.psycopg2-2.5.1
            下载网址：http://initd.org/psycopg/tarballs/PSYCOPG-2-5/psycopg2-2.5.1.tar.gz
          3.django-rest-framework-2.4.1
            github地址：https://github.com/tomchristie/django-rest-framework.git
          
2.安装POSTGRESQL数据库，请看【postgresql_9.1_install.txt】

3.运行程序
   1.注意：
      1.运行此demo，需要确保你的机子上安装了postgresql 9.1（数据库名称为test_db）及python语言和相关依赖库
      2.如果未安装postgresql数据库，可以用sqlite数据库，请修改settings.py文件
         把下面这段代码修改为需要的数据库
        DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql_psycopg2',
              'NAME':'test_db',
              'USER':'postgres',
              'PASSWORD':'postgres',
              'HOST':'localhost',
              'PORT':'5432'
          }
        } 
        
    2.解压demo.tar.gz到相关目录
    3.修改数据库的相关配置，如注意2中所列的部分
    4.导入数据库相关表
        1.切换到demo的相关目录（有manage.py的目录）
        2.导入数据库相关表
        python manage.py syncdb
        3.注意：demo的表结构及功能，请看【demo_table_and_sql.txt】文档
    5.运行此demo
    python manage.py runserver
    
4.测试此demo程序，请看【test_demo.txt】文档

5.以后可以做的
    1.测试添加中文字符是否正确
    2.以名称的方式更新公司表或查询公司表、部门、公司成员
    3.删除成功后，返回提示信息
    4.添加网页界面及相关rest的API的说明文档。
    5.URL查询地址中添加分页查询功能
    6.其他