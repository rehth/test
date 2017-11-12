from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_app(request):
    # 测试应用逻辑
    return render(request, 'new/test_app.html')