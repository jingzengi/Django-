#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/9/5 14:11



from django.contrib import admin
from app02 import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
