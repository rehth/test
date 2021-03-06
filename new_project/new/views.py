from django.shortcuts import render
from django.http import HttpResponse
from new.models import Goods
from new_project import settings
from django.core.mail import send_mail  # 开启邮件服务
from django.views.generic import View   # 类视图


# Create your views here.


def test_app(request):
    # 测试应用逻辑
    return render(request, 'new/test_app.html')


def set_sessions(request):
    # 设置sessions
    request.session['name'] = 'king'
    request.session['pass'] = 'paaa'
    return HttpResponse('sessions 设置成功')


def get_sessions(request):
    # 获取sessions数据
    name = request.session['name']
    ps = request.session['pass']
    return HttpResponse('name:%s, ps:%s' % (name, ps))


def editor(request):
    """ 富文本编辑器测试 """
    return render(request, 'new/test_editor.html')


def db_editor(request):
    """ 富文本编辑器测试 数据库测试 """
    db = request.POST.get('gcontent')
    g = Goods()
    g.goods_info = db
    g.save()   # <p>哈哈，这是啥呀gsdgsdgsdfdsfdsfsd
    # <span style="text-decoration: underline;">dfsdf</span></p>
    return HttpResponse(db)


def send(request):
    """ 发送邮件测试 """
    msg = '<a href="http://www.baidu.com">百度<a/>'
    send_mail('注册激活', '', settings.EMAIL_FROM,
              ['zhangqianjuns@163.com'],
              html_message=msg)
    return HttpResponse('发送成功')


class MyView(View):
    """ 测试类视图 """
    def get(self, request, *args, **kwargs):
        return HttpResponse('my first class views')


# /login
def login(request):
    name = ''
    checked = ''
    # request.COOKIES 是query dict类型
    if 'rem' in request.COOKIES:
        name = request.COOKIES['username']
        checked = 'checked'
    context = {'name': name, 'checked': checked}
    return render(request, 'new/login.html', context)


# /verify
def verify(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'zhang' and password == '123':
        # 设置cookie
        response = HttpResponse('login')
        if request.POST.get('rem') == 'on':
            response.set_cookie('rem', True)
        response.set_cookie('username', username)
        return response
    else:
        return HttpResponse('失败')

