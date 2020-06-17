from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def date(request, city, year):
    # print(request.GET)
    # print(request.GET.get('name'))
    a = request.GET['name']
    print(a)
    return HttpResponse('{}, {}'.format(city, year))

def index(request, name, age):
    name1 = request.GET.get('name')
    age1 = request.GET.getlist('age')

    return HttpResponse(f'{name1}, {age1}index, {name}, {age}')