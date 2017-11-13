from django.shortcuts import render
from django.http import HttpResponse
from new.models import Goods

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
