"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from new import views

urlpatterns = [
    url(r'^test/$', views.test_app),
    # 测试 sessions redis数据库
    url(r'^set/$', views.set_sessions),
    url(r'^get/$', views.get_sessions),
    url(r'^editor$', views.editor),
    # 富文本编辑器测试
    url(r'^db$', views.db_editor),
    # 'zhangqianjuns@163.com'发送邮件测试
    url(r'^send/$', views.send),
    # 测试类视图
    url(r'^class$', views.MyView.as_view()),
    # 测试登陆
    url(r'^login$', views.login),
    url(r'^verify$', views.verify),
]
