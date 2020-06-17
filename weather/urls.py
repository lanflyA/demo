from django.urls import path, re_path
from . import views


# app_name = 'weather'


urlpatterns = [
    re_path(r'^([a-zA-Z]+)/(\d{4})/$', views.date, name='date'),
    re_path(r'^index/(?P<name>\w+)/(?P<age>\d+)/$', views.index, name='index')
]
