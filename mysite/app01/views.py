from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    import datetime
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")
    # return  render(request,"index.html", {"ctime": ctime})
    return HttpResponse('index page...')