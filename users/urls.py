from django.urls import path, re_path
from . import views


app_name = 'users'

urlpatterns = [
    re_path(r'^index/$', views.index, name = 'index'),
    re_path(r'^say/$', views.Say.as_view(), name='say'),
    path('login/', views.login, name='login')
]
