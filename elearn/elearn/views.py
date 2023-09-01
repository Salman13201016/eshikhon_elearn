from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .models import Categories
def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    cat_name = request.POST.get('cat_name')

    cat_obj = Categories()
    cat_obj.name = cat_name

    cat_obj.save()
    messages.success(request, 'Category Inserted successfully')
    return redirect('catadmin')

    