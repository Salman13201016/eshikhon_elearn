
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Categories


def test(request):
    return render(request,'test.html')

def test2(request):
    return HttpResponse("welcome to test2 function")

def index(request):
    cat_name = request.POST.get('cat_name')
    cat_obj = Categories()
    cat_obj.name = cat_name
    cat_obj.save()
    # data = {"name":cat_name}
    return redirect('index')
