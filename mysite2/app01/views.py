from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('我是app01的index页面')