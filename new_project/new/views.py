from django.shortcuts import render
from django.http import HttpResponse

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