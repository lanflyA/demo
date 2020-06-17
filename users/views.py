import datetime

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import  LoginRequiredMixin

# Create your views here.
# from django.contrib.auth import login
from django.utils.decorators import method_decorator

def index(request):

    # dictquery = request.GET
    # print(dictquery)
    # print(type(dictquery))

    url = reverse('weather:index', kwargs={'name': 'sd', 'age': 34 })
    return HttpResponseRedirect(url)
    # return HttpResponse('who are you?')

def my_decorator_2(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper


class SecondMixin(object):
    """ SecondMixin 扩展类 """
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator_2(view)
        return view


class Say(SecondMixin, View):

    def get(self, request):

        return HttpResponse(' SDSD')


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if not all([username, password]):
        return JsonResponse({
            'code': '400',
            'errmsg': '必要参数缺失'
        })

    if password != '123456':
        return JsonResponse({
            'code': '400',
            'errmsg': '用户名或密码错误'
        })


    request.session['username'] = username
    request.session.set_expiry(3600 * 24)
    response = JsonResponse({
        'code': 0,
        'errmsg': 'ok',
        'name': username,
    })

    response.set_cookie('username', username, max_age=30)

    return response